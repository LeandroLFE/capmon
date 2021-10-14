from twitchio.ext.commands import Cog
from typing import Callable
from bot.cogs.events.eventJoin_aux.eventJoin_db_connect import Event_Join_DB_Connect
from bot.messages.general.task_names.nomes_tasks import task_nova_horda_sync

class EventJoin(Cog):

    def __init__(self, bot: Callable):
        super().__init__()
        self.bot = bot
        self.db = Event_Join_DB_Connect()
        self.nome_task_nova_horda_sync = task_nova_horda_sync

    @Cog.event()
    async def event_join(self, channel, user):    
        if channel.name == self.bot.nick or user.name != self.bot.nick:
            return
        self.func_nova_horda_sync = self.bot.cogs['GeraHordas'].nova_horda_sync

        self.bot.logger = self.bot.set_logging(self.bot.canal_thread)
        self.bot.logger.info(f'Joined in {channel.name}')

        dados_canal = {
            "canal_id" : self.bot.canal_thread,
            "nome_canal" : channel.name,
            "nome_idioma" : self.bot.idioma_thread
        }

        _parametros_horda = await self.db.consulta_parametros_hordas_canal(dados_canal)
        self.bot.parametros_horda[dados_canal["canal_id"]] = _parametros_horda

        self.bot.dados_horda[dados_canal["canal_id"]] = {
            "nome_horda" : "", 
            "nome_idioma" : dados_canal["nome_idioma"]
        }

        _tempo_para_proxima_horda = self.bot.random_randint(_parametros_horda["tempo_entre_hordas_min"], _parametros_horda["tempo_entre_hordas_max"])
        _task = self.bot.loop.create_task(self.bot.aguarda(self, _tempo_para_proxima_horda))
        _nome_task = self.nome_task_nova_horda_sync(dados_canal)  
        _task.set_name(_nome_task)
        _task.add_done_callback(self.bot.functools_partial(self.func_nova_horda_sync, dados_canal))