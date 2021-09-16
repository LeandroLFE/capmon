from twitchio.ext.commands import Cog
from bot.cogs.loop_hordas.geraHordas_aux.nova_horda import Nova_horda
from bot.cogs.loop_hordas.geraHordas_aux.warning_final_horda import Warning_final_horda
from bot.cogs.loop_hordas.geraHordas_aux.final_horda import Final_horda
from bot.cogs.loop_hordas.geraHordas_aux.geraHordas_db_connect import Gera_Hordas_DB_Connect

class GeraHordas(Cog):

    def __init__(self, bot : callable):
        super().__init__()
        self.bot = bot
        self.db = Gera_Hordas_DB_Connect()

        self.bot.gera_hordas_nova_horda_sync = self.nova_horda_sync
        self.bot.gera_hordas_warning_final_horda_sync = self.warning_final_horda_sync
        self.bot.gera_hordas_final_horda_sync = self.final_horda_sync
    
        self.nova_horda = Nova_horda(self.bot, self.db)
        self.warning_final_horda = Warning_final_horda(self.bot, self.db)
        self.final_horda = Final_horda(self.bot, self.db)

        self.envia_msg_without_context = self.bot.cogs['Envia_Msg'].envia_msg_without_context

    def nova_horda_sync(self, dados, future):
        if not future.done() or future.cancelled():
            return
        self.bot.loop.create_task(self.nova_horda.nova_horda_async(dados))

    def final_horda_sync(self, dados, future):
        if not future.done() or future.cancelled():
            return
        self.bot.loop.create_task(self.final_horda.final_horda_async(dados))

    def warning_final_horda_sync(self, dados, future):
        if not future.done() or future.cancelled():
            return
        self.bot.loop.create_task(self.warning_final_horda.warning_final_horda_async(dados))