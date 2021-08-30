from typing import Callable
from twitchio.ext.commands import Bot, Cog
from twitchio import Message
from utils.removedor_acentos import remover_acentos

class EventMessage(Cog):
    def __init__(self, bot: Callable, send_msg : Callable = None):
        super().__init__()
        self.bot = bot

    @Cog.event()
    async def event_message(self, message: Message):
        print(message.tags["room-id"])
        print(message.tags["user-id"])
        if message.author.name.lower() == self.bot.nick.lower():
            return
        message.content = remover_acentos(message.content).lower()
        await self.bot.handle_commands(message)