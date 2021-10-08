from twitchio.ext.commands import Bot
from auth.auth import client_id, client_secret, token, nick, prefix, initial_channels
from twitchio.ext.commands.errors import CommandNotFound

class BotBase(Bot):

    def __init__(self):
        super().__init__(client_id=client_id, client_secret=client_secret, token=token,
            nick=nick, prefix=prefix, initial_channels=initial_channels)

    async def event_error(self, error: Exception, data: str):
        self.logger = self.set_logging("errors")
        self.logger.error(f"Erro: {error.args} -> {data}")

    async def event_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            pass       
        self.logger = self.set_logging("errors")
        self.logger.error(f"Erro: {error.args}")

    async def event_message(self, message):
        if message.author.name.lower() == self.nick.lower():
            return
        message.content = self.remover_acentos(message.content).lower()
        await self.handle_commands(message)
