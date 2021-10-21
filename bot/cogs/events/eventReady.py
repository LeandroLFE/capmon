from twitchio.ext.commands import Cog
from bot.cogs.events.eventReady_aux.eventReady_db_connect import Event_Ready_DB_Connect
from bot.methods.aguarda.aguarda import aguarda
from bot.methods.verifica_canal_online.verifica_canal_online import verifica_canal_online
from bot.methods.logging.logging import set_logging
from utils.removedor_acentos import remover_acentos
from bot.methods.logging.logging_aux.prepare_log_msg_without_context import prepare_log_msg_without_context
from utils.import_message_language import import_message_language_by_one
from utils.clear_terminal import clear_terminal
from typing import Callable
from asyncio import all_tasks
from functools import partial
from random import choice, randint
from datetime import datetime

class EventReady(Cog):

    def __init__(self, bot: Callable):
        super().__init__()
        self.db = Event_Ready_DB_Connect()
        self.bot = bot
        self.bot.import_message_language_by_one = import_message_language_by_one
        self.bot.remover_acentos = remover_acentos
        self.bot.clear_terminal = clear_terminal
        self.bot.prepare_log = prepare_log_msg_without_context
        self.bot.aguarda = aguarda
        self.bot.asyncio_all_tasks = all_tasks
        self.bot.random_randint = randint
        self.bot.random_choice = choice
        self.bot.verifica_canal_online = verifica_canal_online
        self.bot.parametros_horda = {}
        self.bot.dados_horda = {}
        self.bot.functools_partial = partial
        self.bot.datetime = datetime
        self.bot.set_logging = set_logging
        self.bot.sessao_ativa = {}

    @Cog.event()
    async def event_ready(self):    
        self.bot.logger = self.bot.set_logging(self.bot.nick)
        self.bot.logger.info(f'Logged in as {self.bot.nick}')
        self.bot.canais_ativos = await self.db.consulta_canais_ativos()
        for canal in self.bot.canais_ativos:
            self.bot.canal_thread = canal["canal_id"]
            self.bot.idioma_thread = canal["idioma"]
            await self.bot.join_channels([canal["nome_canal"]])