from twitchio.ext.commands import Cog, command

from bot.messages.general.available_parameter_list.capaventura_parameters import start_parameter_list, language_parameter_list, stop_parameter_list
from bot.cogs.commands.bot_channel.capaventura_aux.capaventura_db_connect import Capaventura_DB_Connect
from bot.cogs.commands.bot_channel.capaventura_aux.capaventura_start import capaventura_start
from bot.cogs.commands.bot_channel.capaventura_aux.capaventura_stop import capaventura_stop
from bot.cogs.commands.bot_channel.capaventura_aux.capaventura_language import capaventura_language

from db.default_data.dados_tipo_hordas import dados_padrao_tabela_tipo_hordas

class Capaventura(Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.idiomas = []
        self.messages = []

        self.db = Capaventura_DB_Connect()
        
        self.start_parameter_list = start_parameter_list
        self.language_parameter_list = language_parameter_list
        self.stop_parameter_list = stop_parameter_list
        self.dados_padrao_tabela_tipo_hordas = dados_padrao_tabela_tipo_hordas
        self.envia_msg_with_context = self.bot.cogs['Envia_Msg'].envia_msg_with_context

    @command(name='capaventura', aliases=['capadventure'])
    async def capaventura(self, ctx, _cmd='', _opt=''):
        if ctx.channel.name != self.bot.nick:
            return
            
        _cmd = self.bot.remover_acentos(_cmd)
        _opt = self.bot.remover_acentos(_opt)
        _aventureiro = self.bot.remover_acentos(ctx.author.name)

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
            self.error_messages = self.bot.import_message_language_by_one(_idioma_canal, 
            "bot_channel", "capmon_channel_messages", "capmon_channel_messages_error", 
            {
                "aventureiro":_aventureiro,
                "idiomas": [i["nome"] for i in self.idiomas],
                "comandos": self.start_parameter_list() + self.language_parameter_list() + self.stop_parameter_list()    
            })
            await self.envia_msg_with_context(ctx, self.error_messages["invalid_command"])