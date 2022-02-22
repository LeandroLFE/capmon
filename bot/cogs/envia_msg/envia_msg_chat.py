from typing import Callable
from twitchio.ext.commands.meta import Cog
from bot.cogs.envia_msg.envia_msg_aux.envia_msg_chat_db_connect import Envia_MSG_Chat_DB_Connect

class Envia_Msg(Cog):

    def __init__(self, bot: Callable) -> None:
        self.bot = bot
        self.db = Envia_MSG_Chat_DB_Connect()
        self.max_msg_length = 0

    async def envia_msg_whisper(self, dados_aventureiro, msg=''):
        _canal_id = dados_aventureiro["canal_id"]
        _canal_name = dados_aventureiro["nome_canal"]
        _author_name = dados_aventureiro["aventureiro_nome"]
        _max_msg_length = dados_aventureiro["parametros_gerais"]["tamanho_max_msgs"]

        _whisper = f"""PRIVMSG #{_canal_name} :/w {_author_name} {'-'*38}"""
        _msg=  f"""{_whisper} {msg}\r\n"""
        
        while len(_msg) >= _max_msg_length:
            _msg_test = _msg[:_max_msg_length]
            indice = _msg_test.rfind('->')
            _msg_print = _msg_test[:indice-4] if indice > -1 else _msg_test
            await self.bot._connection.send(_msg_print)
            self.bot.logger = self.bot.set_logging(_canal_id)
            self.bot.logger.info(self.bot.prepare_log(_msg_print))
            _msg = _msg[indice-4:]
            _msg =  f"""{_whisper} {_msg}\r\n"""    
            
        else:
            await self.bot._connection.send(_msg)
            self.bot.logger = self.bot.set_logging(_canal_id)
            self.bot.logger.info(self.bot.prepare_log(_msg))

    async def envia_msg_with_context(self, ctx, msg=''):
        _canal_id = ctx.message.tags["room-id"]

        if isinstance(msg, str) == False or msg =='':
            self.bot.logger = self.bot.set_logging(_canal_id)
            self.bot.logger.warning(f"Tipo errado msg: {type(msg)}") if isinstance(msg, str) == False else self.bot.logger.warning(f"Msg vazio: {msg}")
            return

        parametros = {}
        parametros["channel_name"] = ctx.channel.name if self.bot.nick != ctx.channel.name else ctx.author.name
        
        parametros["canal_id"] = _canal_id
        parametros["msg"] = msg
        
        _ultima_msg = await self.db.consulta_ultima_msg(parametros)

        _ultima_msg = _ultima_msg["msg"] if issubclass(type(_ultima_msg), dict) else _ultima_msg

        if _ultima_msg is not None and type(_ultima_msg) != str:
            self.bot.logger = self.bot.set_logging(parametros["canal_id"])
            self.bot.logger.warning(f"Tipo errado ultima_msg: {type(_ultima_msg)}")
            return

        if _ultima_msg is None or (self.bot.remover_acentos(msg) != self.bot.remover_acentos(_ultima_msg)):
            msg = f"""╠{"─"*30}╣ {msg} ╠{"─"*30}╣"""
            await ctx.send(msg)
            await self.db.insert_ultima_msg(parametros) if _ultima_msg is None else await self.db.update_ultima_msg(parametros)
        else:
            data_e_hora_atuais = self.bot.datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
            msg_modificada = f'{msg} ({data_e_hora_em_texto})'
            msg_modificada = f"""╠{"─"*30}╣ {msg_modificada} ╠{"─"*30}╣"""
            await ctx.send(msg_modificada)

        _info_msg = f"""Em resposta a {ctx.message.author.name} que enviou o comando: {ctx.message.content} no canal {ctx.message.channel.name}\nR: {parametros["msg"].strip()}"""
        self.bot.logger = self.bot.set_logging(parametros["canal_id"])
        self.bot.logger.info(self.bot.prepare_log(_info_msg))

    async def envia_msg_without_context(self, channel_data, msg=''):
        _msg =  f"""PRIVMSG #{channel_data["nome_canal"]} :{msg}\r\n"""

        parametros = {
            "canal_id" : channel_data["canal_id"],
            "nome_canal" : channel_data["nome_canal"],
            "msg" : _msg
        }

        _ultima_msg = await self.db.consulta_ultima_msg(parametros)

        if _ultima_msg is None or (self.bot.remover_acentos(_msg) != self.bot.remover_acentos(_ultima_msg)):
            await self.bot._connection.send(_msg)
            await self.db.insert_ultima_msg(parametros) if _ultima_msg is None else await self.db.update_ultima_msg(parametros)    
        else:
            data_e_hora_atuais = self.bot.datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
            _msg = f'{_msg} ({data_e_hora_em_texto})'
            await self.bot._connection.send(_msg)

        self.bot.logger = self.bot.set_logging(parametros["canal_id"])
        self.bot.logger.info(self.bot.prepare_log(_msg))