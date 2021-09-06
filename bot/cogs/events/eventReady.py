from twitchio.ext.commands import Cog
from bot.methods.aguarda.aguarda import aguarda
from bot.methods.nomes_tasks.nomes_tasks import task_nova_horda_sync
from utils.removedor_acentos import remover_acentos
from utils.import_message_language import import_message_language_by_one

from typing import Callable
from asyncio import all_tasks
from functools import partial
from random import randint
from datetime import datetime

class EventReady(Cog):

    def __init__(self, bot: Callable):
        super().__init__()
        self.bot = bot
        self.bot.import_message_language_by_one = import_message_language_by_one
        self.bot.remover_acentos = remover_acentos
        self.bot.aguarda = aguarda
        self.bot.task_nova_horda_sync = task_nova_horda_sync
        self.bot.asyncio_all_tasks = all_tasks
        self.bot.random_randint = randint
        self.bot.functools_partial = partial
        self.bot.datetime = datetime

    @Cog.event()
    async def event_ready(self):    
        print(f'Logged in as | {self.bot.nick}')
