from typing import Callable
from bot.messages.general.task_names.nomes_tasks import task_nova_horda_sync

class Warning_final_horda():

    def __init__(self, bot: Callable, db: Callable):
        self.bot = bot
        self.db = db
        self.envia_msg_without_context = self.bot.cogs['Envia_Msg'].envia_msg_without_context
        self.nome_task_nova_horda_sync = task_nova_horda_sync
        
    async def warning_final_horda_async(self, dados):
        _dados_canal = dados["dados_canal"]
        _dados_horda = dados["dados_horda"]
        _parametros_horda = self.bot.parametros_horda[_dados_canal["canal_id"]] 
        _tempo_warning_final_horda = _parametros_horda["aviso_horda_terminando_em_x_segundos"]

        dados["dados_horda"]["aviso"] = _tempo_warning_final_horda

        _nome_func_tipo_horda = f"""tipo_horda_{_dados_horda["nome_horda"]}"""
        _func_tipo_horda = getattr(self, _nome_func_tipo_horda) 
        await _func_tipo_horda(dados)  

    async def tipo_horda_normal_aleatoria(self, dados):
        _dados_canal = dados["dados_canal"]
        _dados_horda = dados["dados_horda"]

        self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "warning_finishing_normal_horde_message", 
                _dados_horda)
        
        await self.envia_msg_without_context(_dados_canal, self.message)

    async def tipo_horda_elemental(self, dados):
        _dados_canal = dados["dados_canal"]
        _dados_horda = dados["dados_horda"]

        self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "warning_finishing_elemental_horde_message", 
                _dados_horda)
        
        await self.envia_msg_without_context(_dados_canal, self.message)

    async def tipo_horda_capraid(self, dados):
        _dados_canal = dados["dados_canal"]
        _dados_horda = dados["dados_horda"]
        
        self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "warning_finishing_capraid_message", 
                _dados_horda)
        
        await self.envia_msg_without_context(_dados_canal, self.message)

    async def tipo_horda_normal_especifica(self, dados):
        _dados_canal = dados["dados_canal"]
        _dados_horda = dados["dados_horda"]

        self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"], 
                "user_channel", "horde_messages", "warning_finishing_normal_horde_message", 
                _dados_horda)
        
        await self.envia_msg_without_context(_dados_canal, self.message)