from twitchio.ext.commands import Cog, command
from utils.removedor_acentos import remover_acentos
from utils.import_message_language import import_message_language_by_one
from bot.cogs.messages.general.available_parameter_list.capaventura_parameters import start_parameter_list, language_parameter_list, stop_parameter_list
from bot.cogs.commands.bot_channel.capaventura_aux.capaventura_db_connect import Capaventura_DB_Connect
from bot.cogs.commands.bot_channel.capaventura_aux.capaventura_start import capaventura_start
from bot.cogs.commands.bot_channel.capaventura_aux.capaventura_stop import capaventura_stop
from bot.cogs.commands.bot_channel.capaventura_aux.capaventura_language import capaventura_language

class Capaventura(Cog):

    def __init__(self, bot, send_msg):
        super().__init__()
        self.bot = bot
        self.send_msg = send_msg

        self.idiomas = []
        self.messages = []

        self.db = Capaventura_DB_Connect()

        self.remover_acentos = remover_acentos
        self.import_message_language_by_one = import_message_language_by_one
        self.start_parameter_list = start_parameter_list
        self.language_parameter_list = language_parameter_list
        self.stop_parameter_list = stop_parameter_list
        

    @command(name='capaventura', aliases=['capadventure'])
    async def capaventura(self, ctx, _cmd='', _opt=''):
        _cmd = self.remover_acentos(_cmd)
        _opt = self.remover_acentos(_opt)
        _aventureiro = self.remover_acentos(ctx.author.name)

        self.idiomas = await self.db.consulta_todos_idiomas()

        _idioma_canal = [i["nome"] for i in self.idiomas if i["nome"] == _opt]
        _idioma_canal = "english" if _idioma_canal == [] else _idioma_canal[0]

        if _cmd in start_parameter_list():
            await capaventura_start(self, ctx, _idioma_canal)

        elif _cmd in language_parameter_list():
            await capaventura_language(self, ctx, _opt)

        elif _cmd in stop_parameter_list():
            await capaventura_stop(self, ctx)
        else:
            self.error_messages = self.import_message_language_by_one(_idioma_canal, 
            "bot_channel", "capmon_channel_messages", "capmon_channel_messages_error", 
            {
                "aventureiro":_aventureiro,
                "idiomas": [i["nome"] for i in self.idiomas],
                "comandos": self.start_parameter_list() + self.language_parameter_list() + self.stop_parameter_list()    
            })
            await self.send_msg.envia_msg_with_context(ctx, self.error_messages["invalid_command"])