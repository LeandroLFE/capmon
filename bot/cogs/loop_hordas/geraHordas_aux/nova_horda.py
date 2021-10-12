from bot.messages.general.task_names.nomes_tasks import task_nova_horda_sync, task_fim_horda_sync, task_fim_horda_x_seg_antes_sync

class Nova_horda():

    def __init__(self, bot, db):
        self.bot = bot
        self.db = db
        self.envia_msg_without_context = self.bot.cogs['Envia_Msg'].envia_msg_without_context
        self.nome_task_nova_horda_sync = task_nova_horda_sync
        self.nome_task_warning_final_horda_sync = task_fim_horda_x_seg_antes_sync
        self.nome_task_final_horda_sync = task_fim_horda_sync

    async def nova_horda_async(self, dados_canal):
        _canal_online = await self.bot.verifica_canal_online(self, dados_canal)
        _nome_idioma = await self.db.consulta_idioma_por_canal_id(dados_canal)
        dados_canal["nome_idioma"] = _nome_idioma["nome"]
        _parametros_horda = self.bot.parametros_horda[dados_canal["canal_id"]] 

        # if not _canal_online:
        #     _tempo_para_proxima_horda = self.bot.random_randint(_parametros_horda["tempo_entre_hordas_min"], _parametros_horda["tempo_entre_hordas_max"])
        #     _task = self.bot.loop.create_task(self.bot.aguarda(self, _tempo_para_proxima_horda))
        #     _nome_task = self.nome_task_nova_horda_sync(dados_canal)  
        #     _task.set_name(_nome_task)
        #     _task.add_done_callback(self.bot.functools_partial(self.bot.gera_hordas_nova_horda_sync, dados_canal))
        #     return

        await self.db.update_tipo_horda_ativa(dados_canal)  
        
        dados_canal["horda_ativa"] = 1
        await self.db.update_ativa_horda(dados_canal)  
        _nome_horda = await self.db.seleciona_horda_ativa_canal(dados_canal)

        _nome_func_tipo_horda = f"""tipo_horda_{_nome_horda["nome"]}"""
        _func_tipo_horda = getattr(self, _nome_func_tipo_horda) 
        _dados_horda = await _func_tipo_horda(dados_canal)  

        _tempo_para_final_horda = self.bot.random_randint(_parametros_horda["tempo_horda_min"], _parametros_horda["tempo_horda_max"])
        _tempo_warning_horda = 0 if _tempo_para_final_horda -_parametros_horda["aviso_horda_terminando_em_x_segundos"] < 0 else  _tempo_para_final_horda -_parametros_horda["aviso_horda_terminando_em_x_segundos"]
        
        _task = self.bot.loop.create_task(self.bot.aguarda(self, _tempo_para_final_horda))
        _task_warning = self.bot.loop.create_task(self.bot.aguarda(self, _tempo_warning_horda))
        
        _nome_task = self.nome_task_final_horda_sync(dados_canal)  
        _nome_task_warning = self.nome_task_warning_final_horda_sync(dados_canal)  
        
        _task.set_name(_nome_task)
        _task_warning.set_name(_nome_task_warning)

        self.bot.dados_horda[dados_canal["canal_id"]] = _dados_horda

        _task.add_done_callback(self.bot.functools_partial(self.bot.gera_hordas_final_horda_sync, dados_canal))     
        _task_warning.add_done_callback(self.bot.functools_partial(self.bot.gera_hordas_warning_final_horda_sync, dados_canal))    
       
    async def tipo_horda_normal_aleatoria(self, dados_canal):

        _criatura = await self.db.seleciona_criatura_aleatoria(dados_canal)

        _parametros_horda = self.bot.parametros_horda[dados_canal["canal_id"]] 

        _duracao = self.bot.random_randint(_parametros_horda["tempo_horda_min"], _parametros_horda["tempo_horda_max"]) 

        dados_horda = {
            "nome_idioma" : dados_canal["nome_idioma"],
            "nome_horda" : "normal_aleatoria",
            "criatura" : _criatura,
            "criaturas" : [],
            "aventureiros" : [],
            "capturados" : [],
            "capraid" : {},
            "duracao" : _duracao,
        }
        
        self.message = self.bot.import_message_language_by_one(dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "new_normal_horde_message", 
                dados_horda)
        
        await self.envia_msg_without_context(dados_canal, self.message)

        return dados_horda

    async def tipo_horda_elemental(self, dados_canal):

        _parametros_horda = self.bot.parametros_horda[dados_canal["canal_id"]]
        _duracao = self.bot.random_randint(_parametros_horda["tempo_horda_min"], _parametros_horda["tempo_horda_max"]) 

        _atributos = await self.db.seleciona_todos_atributos(dados_canal)
        _custos = await self.db.seleciona_todos_custos(dados_canal)

        _list_atributos = [a["ref"] for a in _atributos]
        _list_custos = [c["ref"] for c in _custos]

        dados_horda = {
            "nome_idioma" : dados_canal["nome_idioma"],
            "nome_horda" : "elemental",
            "aventureiros" : [],
            "capturados" : [],
            "capraid" : {},
            "duracao" : _duracao,
        }

        dados_horda["ref_atributo"] = self.bot.random_choice(_list_atributos)
        dados_horda["custo"] = self.bot.random_choice(_list_custos)
        _criaturas = await self.db.seleciona_criaturas_atributo(dados_horda)
        
        while _criaturas == []:
            dados_horda["ref_atributo"] = self.bot.random_choice(_list_atributos)
            dados_horda["custo"] = self.bot.random_choice(_list_custos)
            _criaturas = await self.db.seleciona_criaturas_atributo(dados_horda)

        dados_horda["nome_tipo"] = _criaturas[0]["nome_tipo"]        
        dados_horda["criaturas"] = _criaturas

        _atributo = await self.db.seleciona_atributo_por_ref(dados_horda)
        dados_horda["atributo"] = _atributo["nome"]

        self.message = self.bot.import_message_language_by_one(dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "new_elemental_horde_message", 
                dados_horda)
        
        await self.envia_msg_without_context(dados_canal, self.message)

        return dados_horda

    async def tipo_horda_capraid(self, dados_canal):

        _criatura = await self.db.seleciona_criatura_aleatoria_lendaria(dados_canal)

        _parametros_horda = self.bot.parametros_horda[dados_canal["canal_id"]] 

        _duracao = _parametros_horda["tempo_horda_max"]

        _capraid = {

        }

        dados_horda = {
            "nome_idioma" : dados_canal["nome_idioma"],
            "nome_horda" : "capraid",
            "criatura" : _criatura,
            "criaturas" : [],
            "aventureiros" : [],
            "capturados" : [],
            "capraid" : _capraid,
            "duracao" : _duracao,
        }
        
        self.message = self.bot.import_message_language_by_one(dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "new_capraid_message", 
                dados_horda)
        
        await self.envia_msg_without_context(dados_canal, self.message)

        return dados_horda

    async def tipo_horda_normal_especifica(self, dados_canal, criatura):

        _parametros_horda = self.bot.parametros_horda[dados_canal["canal_id"]] 

        _duracao = self.bot.random_randint(_parametros_horda["tempo_horda_min"], _parametros_horda["tempo_horda_max"]) 

        dados_horda = {
            "nome_horda" : "normal_especifica",
            "criatura" : criatura,
            "criaturas" : [],
            "aventureiros" : [],
            "capturados" : [],
            "capraid" : {},
            "duracao" : _duracao,
        }
        
        self.message = self.bot.import_message_language_by_one(dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "new_normal_horde_message", 
                dados_horda)
        
        await self.envia_msg_without_context(dados_canal, self.message)

        return dados_horda


