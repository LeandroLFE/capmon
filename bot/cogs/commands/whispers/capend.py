from twitchio.ext.commands import Cog, command

class Capend(Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.envia_msg_whisper = self.bot.cogs['Envia_Msg'].envia_msg_whisper

    async def listen_whisper(self, _dados_whisper):

        _aventureiro_id_test = f"""capshop_aventureiro_id_{_dados_whisper["aventureiro_id"]}"""
        
        _tasks = self.bot.asyncio_all_tasks(self.bot.loop)
        _sessao = [task for task in _tasks if _aventureiro_id_test in task.get_name()]

        if _sessao == []:
            return

        if _dados_whisper["aventureiro_id"] not in self.bot.sessao_ativa.keys():
            return

        _nome_idioma = self.bot.sessao_ativa[_dados_whisper["aventureiro_id"]]["dados"]["nome_idioma"]

        _sessao[0].cancel()
        _dados_aventureiro = self.bot.sessao_ativa.pop(_dados_whisper["aventureiro_id"], None)

        self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                               "user_channel", "capshop_messages", "end_session",
                                                               {}
                                                               )
        await self.envia_msg_whisper(_dados_aventureiro["dados"]["aventureiro"], self.message)