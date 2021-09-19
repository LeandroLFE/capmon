from twitchio.ext.commands import Bot
from auth.auth import client_id, client_secret, token, nick, prefix, initial_channels
from twitchio.ext.commands.errors import CommandNotFound

class BotBase(Bot):

    def __init__(self):
        super().__init__(client_id=client_id, client_secret=client_secret, token=token,
            nick=nick, prefix=prefix, initial_channels=initial_channels)

    async def event_error(self, error: Exception, data: str):
        await super().event_error(error, data=data)
        self.logger["bot-errors"].error(f"Erro: {error} -> {data}")

    async def event_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            pass
        self.logger["bot-errors"].error(f"Erro: {error}")
