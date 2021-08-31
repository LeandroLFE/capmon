from typing import Callable
from utils.removedor_acentos import remover_acentos
from bot.utils.envia_msg.envia_msg_aux.envia_msg_chat_db_connect import Envia_MSG_Chat_DB_Connect
from datetime import datetime

class Envia_Msg:

    def __init__(self, bot: Callable) -> None:
        self.bot = bot
        self.db = Envia_MSG_Chat_DB_Connect()

    async def envia_msg_with_context(self, ctx, msg=''):
        if isinstance(msg, str) == False or msg =='':
            print(f"Tipo errado msg: {type(msg)}") if isinstance(msg, str) == False else print(f"Msg vazio: {msg}")
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
            print(f"Tipo errado ultima_msg: {type(_ultima_msg)}")
            return

        if _ultima_msg == None or (remover_acentos(msg) != remover_acentos(_ultima_msg)):
            await ctx.send(msg)
            await self.db.insert_ultima_msg(parametros) if _ultima_msg == None else await self.db.update_ultima_msg(parametros)
        else:
            data_e_hora_atuais = datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
            msg_modificada = f'{msg} ({data_e_hora_em_texto})'
            await ctx.send(msg_modificada)

    async def envia_msg_without_context(self, channel_name, msg=''):
        parametros = {}

        parametros["channel_name"] = channel_name 

        _channel_id = await self.db.consulta_channel_id({
            "nome_canal" : parametros["channel_name"]
        })

        if _channel_id != None:
            parametros["canal_id"] = _channel_id  
        else:
            print("Canal inválido") 
            return

        parametros["msg"] = msg
        _ultima_msg = await self.db.consulta_ultima_msg(parametros)

        if _ultima_msg == None or (remover_acentos(msg) != remover_acentos(_ultima_msg)):
            await self.bot._ws.send_privmsg(channel_name, msg)
            await self.db.insert_ultima_msg(parametros) if _ultima_msg == None else await self.db.update_ultima_msg(parametros)    
        else:
            data_e_hora_atuais = datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
            msg = f'{msg} ({data_e_hora_em_texto})'

            await self.bot._ws.send_privmsg(channel_name, msg)