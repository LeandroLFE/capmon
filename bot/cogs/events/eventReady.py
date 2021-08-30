from typing import Callable
from twitchio.ext.commands import Cog

class EventReady(Cog):

    def __init__(self, bot: Callable, send_msg : Callable = None):
        super().__init__()
        self.bot = bot

    @Cog.event()
    async def event_ready(self):    
        print(f'Logged in as | {self.bot.nick}')
