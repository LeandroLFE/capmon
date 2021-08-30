from twitchio.ext.commands import Bot
from auth.auth import client_id, client_secret, token, nick, prefix, initial_channels

class BotBase(Bot):

    def __init__(self):
        super().__init__(client_id=client_id, client_secret=client_secret, token=token,
            nick=nick, prefix=prefix, initial_channels=initial_channels)