from typing import Callable
from bot.messages.general.task_names.nomes_tasks import task_nova_horda_sync
class Final_horda():

    def __init__(self, bot: Callable, db: Callable):
        self.bot = bot
        self.db = db
        self.envia_msg_without_context = self.bot.cogs['Envia_Msg'].envia_msg_without_context
        self.nome_task_nova_horda_sync = task_nova_horda_sync

    async def atualiza_capcoins_aventureiros(self, aventureiros = [], _parametros_aventureiro_canal = {}):

        for a in aventureiros:
            a["cont_hordas_atual"] = a["tabela"]["cont_hordas_atual"] + 1
            a["cont_sequencia_atual"] = a["tabela"]["cont_sequencia_atual"] + 1

            if a["cont_hordas_atual"] >= _parametros_aventureiro_canal["cont_hordas_para_add_capcoins"]:
                a["capcoins"] += self.bot.random_randint(_parametros_aventureiro_canal["add_capcoins_min"], _parametros_aventureiro_canal["add_capcoins_max"])
                a["cont_hordas_atual"] = 0

            if a["cont_sequencia_atual"] >= _parametros_aventureiro_canal["cont_sequencia_para_add_capcoins_bonus"]:
                a["capcoins"] += self.bot.random_randint(_parametros_aventureiro_canal["add_capcoins_bonus_min"], _parametros_aventureiro_canal["add_capcoins_bonus_max"])
                a["cont_sequencia_atual"] = 0

        return aventureiros
        
    async def final_horda_async(self, dados_canal):
        _dados_canal = dados_canal
        _dados_horda = self.bot.dados_horda[dados_canal["canal_id"]]
        _parametros_horda = self.bot.parametros_horda[_dados_canal["canal_id"]]
        _tempo_para_proxima_horda = self.bot.random_randint(_parametros_horda["tempo_entre_hordas_min"], _parametros_horda["tempo_entre_hordas_max"])
        
        dados = {
            "dados_canal" : dados_canal,
            "dados_horda" : _dados_horda
        }

        dados["dados_horda"]["tempo_espera"] = _tempo_para_proxima_horda

        _dados_canal["horda_ativa"] = 0
        await self.db.update_ativa_horda(_dados_canal)  

        _nome_func_tipo_horda = f"""tipo_horda_{_dados_horda["nome_horda"]}"""
        _func_tipo_horda = getattr(self, _nome_func_tipo_horda) 
        await _func_tipo_horda(dados)  

        await self.db.update_tipo_hordas_reset(_dados_canal)
        await self.db.update_tipo_hordas_elemental(_dados_canal)
        await self.db.update_tipo_hordas_capraid(_dados_canal)

        if _dados_horda["capturados"] != []:
            _parametros_aventureiro = await self.db.consulta_parametros_aventureiros_canal(dados_canal)
            _dados_horda["aventureiros"] = await self.atualiza_capcoins_aventureiros(_dados_horda["aventureiros"], _parametros_aventureiro)
            _dados_horda["aventureiros"][0]["canal_id"] = dados_canal["canal_id"]
            await self.db.insert_update_aventureiros(_dados_horda["aventureiros"])

            _quem_capturou = [c for c in _dados_horda["capturados"] if c["id_criatura"] != 0]

            if _quem_capturou != []:
                _dados_horda["capturados"][0]["canal_id"] = dados_canal["canal_id"]
                await self.db.insert_update_capturados(_quem_capturou)

            await self.db.reset_cont_sequencia_outros_aventureiros({
                "canal_id" : dados_canal["canal_id"],
                "aventureiros_id" : ", ".join((a["aventureiro_id"] for a in _dados_horda["aventureiros"])) 
            })

        self.bot.dados_horda[dados_canal["canal_id"]]["nome_horda"] = ""
        _task = self.bot.loop.create_task(self.bot.aguarda(self, _tempo_para_proxima_horda))
        _nome_task = self.nome_task_nova_horda_sync(_dados_canal)  
        _task.set_name(_nome_task)
        _task.add_done_callback(self.bot.functools_partial(self.bot.gera_hordas_nova_horda_sync, _dados_canal))  

    async def tipo_horda_normal_aleatoria(self, dados):
        _dados_canal = dados["dados_canal"]
        _dados_horda = dados["dados_horda"]

        _canal_online = await self.bot.verifica_canal_online(self, _dados_canal)

        if not _canal_online:
            self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "end_normal_horde_message_offline_channel", 
                _dados_horda)
        
            await self.envia_msg_without_context(_dados_canal, self.message)
            
            return

        self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "end_normal_horde_message", 
                _dados_horda)
        
        await self.envia_msg_without_context(_dados_canal, self.message)

    async def tipo_horda_elemental(self, dados):
        _dados_canal = dados["dados_canal"]
        _dados_horda = dados["dados_horda"]

        _canal_online = await self.bot.verifica_canal_online(self, _dados_canal)

        if not _canal_online:
            self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "end_elemental_horde_message_offline_channel", 
                _dados_horda)
        
            await self.envia_msg_without_context(_dados_canal, self.message)
            
            return

        self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "end_elemental_horde_message", 
                _dados_horda)
        
        await self.envia_msg_without_context(_dados_canal, self.message)

    async def tipo_horda_capraid(self, dados):
        _dados_canal = dados["dados_canal"]
        _dados_horda = dados["dados_horda"]

        _canal_online = await self.bot.verifica_canal_online(self, _dados_canal)

        if not _canal_online:
            self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "end_capraid_defeat_message_offline_channel", 
                _dados_horda)
        
            await self.envia_msg_without_context(_dados_canal, self.message)
            
            return
        
        self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "end_capraid_defeat_message", 
                _dados_horda)
        
        await self.envia_msg_without_context(_dados_canal, self.message)

    async def tipo_horda_normal_especifica(self, dados):
        _dados_canal = dados["dados_canal"]
        _dados_horda = dados["dados_horda"]

        _canal_online = await self.bot.verifica_canal_online(self, _dados_canal)

        if not _canal_online:
            self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "end_normal_horde_message_offline_channel", 
                _dados_horda)
        
            await self.envia_msg_without_context(_dados_canal, self.message)
            
            return

        self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "end_normal_horde_message", 
                _dados_horda)
        
        await self.envia_msg_without_context(_dados_canal, self.message)