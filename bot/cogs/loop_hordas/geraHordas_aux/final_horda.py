from typing import Callable
from bot.messages.general.task_names.nomes_tasks import task_nova_horda_sync
class Final_horda():

    def __init__(self, bot: Callable, db: Callable):
        self.bot = bot
        self.db = db
        self.envia_msg_without_context = self.bot.cogs['Envia_Msg'].envia_msg_without_context
        self.nome_task_nova_horda_sync = task_nova_horda_sync
        
    async def final_horda_async(self, dados):
        _dados_canal = dados["dados_canal"]
        _dados_horda = dados["dados_horda"]
        _parametros_horda = self.bot.parametros_horda[_dados_canal["canal_id"]]
        _tempo_para_proxima_horda = self.bot.random_randint(_parametros_horda["tempo_entre_hordas_min"], _parametros_horda["tempo_entre_hordas_max"])

        dados["dados_horda"]["tempo_espera"] = _tempo_para_proxima_horda

        _dados_canal["horda_ativa"] = 0
        await self.db.update_ativa_horda(_dados_canal)  
        await self.db.update_tipo_hordas_elemental(_dados_canal)
        await self.db.update_tipo_hordas_capraid(_dados_canal)

        _nome_func_tipo_horda = f"""tipo_horda_{_dados_horda["nome_horda"]}"""
        _func_tipo_horda = getattr(self, _nome_func_tipo_horda) 
        await _func_tipo_horda(dados)  
         
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
                "adventure_channel", "horde_messages", "end_normal_horde_message_offline_channel", 
                _dados_horda)
        
            await self.envia_msg_without_context(_dados_canal, self.message)
            
            return

        self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "adventure_channel", "horde_messages", "end_normal_horde_message", 
                _dados_horda)
        
        await self.envia_msg_without_context(_dados_canal, self.message)

    async def tipo_horda_elemental(self, dados):
        _dados_canal = dados["dados_canal"]
        _dados_horda = dados["dados_horda"]

        _canal_online = await self.bot.verifica_canal_online(self, _dados_canal)

        if not _canal_online:
            self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "adventure_channel", "horde_messages", "end_elemental_horde_message_offline_channel", 
                _dados_horda)
        
            await self.envia_msg_without_context(_dados_canal, self.message)
            
            return

        self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "adventure_channel", "horde_messages", "end_elemental_horde_message", 
                _dados_horda)
        
        await self.envia_msg_without_context(_dados_canal, self.message)

    async def tipo_horda_capraid(self, dados):
        _dados_canal = dados["dados_canal"]
        _dados_horda = dados["dados_horda"]

        _canal_online = await self.bot.verifica_canal_online(self, _dados_canal)

        if not _canal_online:
            self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "adventure_channel", "horde_messages", "end_capraid_defeat_message_offline_channel", 
                _dados_horda)
        
            await self.envia_msg_without_context(_dados_canal, self.message)
            
            return
        
        self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "adventure_channel", "horde_messages", "end_capraid_defeat_message", 
                _dados_horda)
        
        await self.envia_msg_without_context(_dados_canal, self.message)

    async def tipo_horda_normal_especifica(self, dados):
        _dados_canal = dados["dados_canal"]
        _dados_horda = dados["dados_horda"]

        _canal_online = await self.bot.verifica_canal_online(self, _dados_canal)

        if not _canal_online:
            self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "adventure_channel", "horde_messages", "end_normal_horde_message_offline_channel", 
                _dados_horda)
        
            await self.envia_msg_without_context(_dados_canal, self.message)
            
            return

        self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "adventure_channel", "horde_messages", "end_normal_horde_message", 
                _dados_horda)
        
        await self.envia_msg_without_context(_dados_canal, self.message)