from twitchio.ext.commands import Bot
from auth.auth import client_id, client_secret, token, nick, prefix, initial_channels
from twitchio.ext.commands.errors import CommandNotFound

class BotBase(Bot):

    def __init__(self):
        # super().__init__(client_id=client_id, client_secret=client_secret, token=token,
        #     nick=nick, prefix=prefix, initial_channels=initial_channels)
        super().__init__(token=token, prefix=prefix, initial_channels=initial_channels)

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
            if message is None:
                return
            if message.author is None:
                return
            self.logger = self.set_logging("errors")
            self.logger.error(f"Event message error: {e.args}")
            return

        else:
            message.content = self.remover_acentos(message.content)
            await self.handle_commands(message)

    async def event_raw_data(self, data):
        whisper_bot = f'WHISPER {self.nick} :'
        if not whisper_bot in data:
            return
        
        _raw_command = self.remover_acentos(data[data.find(whisper_bot) 
            + len(whisper_bot):data.find('\r\n')].replace("#", "")
            )

        if whisper_bot.lower() in _raw_command:
            return

        _raw_command = _raw_command.split()
        _user_id = data[data.find("user-id=", 1) + len("user-id=") : data.find(";user-type=", 1)]
        _user_name = data[data.find("name=", 1) + len("name=") : data.find(";emotes=", 1)]
        
        _aventureiro_id_test = f"_aventureiro_id_{_user_id}"

        _tasks = self.asyncio_all_tasks(self.loop)
        _sessao_task = [task for task in _tasks if _aventureiro_id_test in task.get_name()]

        if _sessao_task == []:
            return
        
        _nome_sessao = _sessao_task[0].get_name()
        _canal_id = _nome_sessao[_nome_sessao.find("canal_id_") + len("canal_id_") : _nome_sessao.find(_aventureiro_id_test)]

        _dados_whisper = {
            "aventureiro_id" : _user_id,
            "aventureiro_nome" : _user_name,
            "nome_canal" : self.nick,
            "comando" : _raw_command,
            "canal_id" : _canal_id,
        }

        try:
            _func_whisper = getattr(self.cogs[_raw_command[0].capitalize()], "listen_whisper") 
            await _func_whisper(_dados_whisper) 
        
        except Exception as e:
            return

if __name__ == "__main__":
    bot = Bot()   
    bot.run()