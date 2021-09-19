from typing import Callable
from twitchio.ext.commands.meta import Cog
from bot.cogs.envia_msg.envia_msg_aux.envia_msg_chat_db_connect import Envia_MSG_Chat_DB_Connect

class Envia_Msg(Cog):

    def __init__(self, bot: Callable) -> None:
        self.bot = bot
        self.db = Envia_MSG_Chat_DB_Connect()

    async def envia_msg_with_context(self, ctx, msg=''):
        if isinstance(msg, str) == False or msg =='':
            self.bot.logger.warning(f"Tipo errado msg: {type(msg)}") if isinstance(msg, str) == False else self.bot.logger.warning(f"Msg vazio: {msg}")
            return
        
        parametros = {}

        parametros["channel_name"] = ctx.channel.name if self.bot.nick != ctx.channel.name else ctx.author.name
        
        _channel_id = await self.db.consulta_channel_id({
            "nome_canal" : parametros["channel_name"]
        })

        parametros["canal_id"] = _channel_id["canal_id"] if _channel_id != None else ctx.author.id
        parametros["msg"] = msg
        
        _ultima_msg = await self.db.consulta_ultima_msg(parametros)

        _ultima_msg = _ultima_msg["msg"] if issubclass(type(_ultima_msg), dict) else _ultima_msg

        if _ultima_msg != None and type(_ultima_msg) != str:
            self.bot.logger.warning(f"Tipo errado ultima_msg: {type(_ultima_msg)}")
            return

        if _ultima_msg == None or (self.bot.remover_acentos(msg) != self.bot.remover_acentos(_ultima_msg)):
            await ctx.send(msg)
            await self.db.insert_ultima_msg(parametros) if _ultima_msg == None else await self.db.update_ultima_msg(parametros)
        else:
            data_e_hora_atuais = self.bot.datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
            msg_modificada = f'{msg} ({data_e_hora_em_texto})'
            await ctx.send(msg_modificada)

        _info_msg = f"""Em resposta a {ctx.message.author.name} que enviou o comando: {ctx.message.content} no canal {ctx.message.channel.name}\nR: {parametros["msg"].strip()}"""
        self.bot.logger[parametros["canal_id"]].info(_info_msg)

    async def envia_msg_without_context(self, channel_data, msg=''):
        _msg =  f"""PRIVMSG #{channel_data["nome_canal"]} :{msg}\r\n"""

        parametros = {
            "canal_id" : channel_data["canal_id"],
            "nome_canal" : channel_data["nome_canal"],
            "msg" : _msg
        }

        _ultima_msg = await self.db.consulta_ultima_msg(parametros)

        if _ultima_msg == None or (self.bot.remover_acentos(_msg) != self.bot.remover_acentos(_ultima_msg)):
            await self.bot._connection.send(_msg)
            await self.db.insert_ultima_msg(parametros) if _ultima_msg == None else await self.db.update_ultima_msg(parametros)    
        else:
            data_e_hora_atuais = self.bot.datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
            _msg = f'{_msg} ({data_e_hora_em_texto})'
            await self.bot._connection.send(_msg)

        self.bot.logger[parametros["canal_id"]].info(self.bot.prepare_log(_msg))