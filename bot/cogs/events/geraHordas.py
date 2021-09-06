from twitchio.ext.commands import Cog
from bot.methods.loop_hordas.nova_horda import nova_horda_sync_impl

class GeraHordas(Cog):

    def __init__(self, bot : callable):
        super().__init__()
        self.bot = bot

    def nova_horda_sync(self, dados, future):
        if not future.done():
            return

        self.bot.loop.create_task(nova_horda_sync_impl(self, dados, future))