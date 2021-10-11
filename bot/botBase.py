from twitchio.ext.commands import Bot
from auth.auth import client_id, client_secret, token, nick, prefix, initial_channels
from twitchio.ext.commands.errors import CommandNotFound

class BotBase(Bot):

    def __init__(self):
        super().__init__(client_id=client_id, client_secret=client_secret, token=token,
            nick=nick, prefix=prefix, initial_channels=initial_channels)

    async def event_error(self, error: Exception, data: str):
        self.logger = self.set_logging("errors")
        self.logger.error(f"Event error: {error.args} -> {data}")

    async def event_command_error(self, ctx, error):
        if type(error) == CommandNotFound:
            return      
        self.logger = self.set_logging("errors")
        self.logger.error(f"Event command error: {error.args}")

    async def event_message(self, message):
        try:
            if message.author.name == self.nick:
                return
        
        except Exception as e:
            if message == None:
                return
            if message.author == None:
                return
            self.logger = self.set_logging("errors")
            self.logger.error(f"Event message error: {e.args}")
            return

        else:
            message.content = self.remover_acentos(message.content).lower()
            await self.handle_commands(message)
