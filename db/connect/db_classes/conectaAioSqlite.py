from aiosqlite import connect
from db.connect.interface.conectaDB import ConectaDB
from utils.dict_factory_sqlite3 import dict_factory

class ConectaAioSQLite(ConectaDB):

    def __init__(self, path: str = "db/db_name.db"):
        super().__init__(path)
        self.path = path

    def create_or_drop_table(self, func : object)->object:
        botPatch = self.path
        async def _create_table(self: object, dados: str = "")->None:
            async with connect(botPatch) as db:
                script = await func(self, dados)
                await db.executescript(script)
                await db.commit()
        return _create_table
    
    def insert_table_one_line(self, func : object)->object:
        botPatch = self.path
        async def _insert_table(self: object, dados: dict = {})->None:
            async with connect(botPatch) as db:
                script = await func(self, dados)
                await db.execute(script, dados)
                await db.commit()
        return _insert_table

    def insert_table_many_lines(self, func : object)->object:
        botPatch = self.path
        async def _insert_table(self: object, dados: list = []) ->None:
            async with connect(botPatch) as db:
                script = await func(self, dados[0])
                await db.executemany(script, dados)
                await db.commit()
        return _insert_table

    def update_table(self, func : object)->object:
        botPatch = self.path
        async def _update_table(self: object, dados: dict = {})->None:
            async with connect(botPatch) as db:
                script = await func(self, dados)
                await db.execute(script, dados)
                await db.commit()
        return _update_table

    def delete_table(self, func : object)->object:
        botPatch = self.path
        async def _delete_table(self: object, dados: dict = {})->None:
            with connect(botPatch) as db:
                script = await func(self, dados)
                await db.execute(script, dados)
                await db.commit()
        return _delete_table

    def select_table_many_data(self, func : object)->object:
        botPatch = self.path
        async def _select_table_many_data(self : object = None, dados = {}):
            async with connect(botPatch) as db:
                db.row_factory = dict_factory
                cur = await db.cursor()
                script = await func(self, dados)
                await cur.execute(script, dados)
                rows = await cur.fetchall()
                return rows
        return _select_table_many_data

    def select_table_one_data(self, func : object)->object:
        botPatch = self.path
        async def _select_table_one_data(self : object = None, dados = {}):
            async with connect(botPatch) as db:
                db.row_factory = dict_factory
                cur = await db.cursor()
                script = await func(self, dados)
                await cur.execute(script, dados)
                rows = await cur.fetchone()
                return rows
        return _select_table_one_data
