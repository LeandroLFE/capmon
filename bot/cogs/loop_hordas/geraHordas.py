from twitchio.ext.commands import Cog
from bot.cogs.loop_hordas.geraHordas_aux.nova_horda import nova_horda_impl

class GeraHordas(Cog):

    def __init__(self, bot : callable):
        super().__init__()
        self.bot = bot

    def nova_horda_sync(self, dados, future):
        if not future.done():
            return

        self.bot.loop.create_task(nova_horda_impl(self, dados, future))