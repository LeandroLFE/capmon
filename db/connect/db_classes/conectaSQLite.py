from sqlite3 import connect
from db.connect.interface.conectaDB import ConectaDB
from utils.dict_factory_sqlite3 import dict_factory

class ConectaSQLite(ConectaDB):

    def __init__(self, path: str = "db/db_name.db"):
        super().__init__(path)

    def create_or_drop_table(self, func : object)->object:
        botPatch = self.path
        def _create_table(self: object, dados: str = "")->None:
            with connect(botPatch) as db:
                script = func(self, dados)
                db.executescript(script)
                db.commit()
        return _create_table

    def insert_table_one_line(self, func : object)->object:
        botPatch = self.path
        def _insert_table(self: object, dados: dict = {})->None:
            with connect(botPatch) as db:
                script = func(self, dados)
                db.execute(script, dados)
                db.commit()
        return _insert_table

    def insert_table_many_lines(self, func : object)->object:
        botPatch = self.path
        def _insert_table(self: object, dados: list = []) ->None:
            with connect(botPatch) as db:
                script = func(self, dados[0])
                db.executemany(script, dados)
                db.commit()
        return _insert_table

    def update_table(self, func : object)->object:
        botPatch = self.path
        def _update_table(self: object, dados: dict = {})->None:
            with connect(botPatch) as db:
                script = func(self, dados)
                db.execute(script, dados)
                db.commit()
        return _update_table

    def delete_table(self, func : object)->object:
        botPatch = self.path
        def _delete_table(self: object, dados: dict = {})->None:
            with connect(botPatch) as db:
                script = func(self, dados)
                db.execute(script, dados)
                db.commit()
        return _delete_table

    def select_table_many_data(self, func : object)->object:
        botPatch = self.path
        def _select_table_many_data(self : object = None, dados = {}):
            with connect(botPatch) as db:
                db.row_factory = dict_factory    
                cur = db.cursor()
                script = func(self, dados)
                cur.execute(script, dados)
                rows = cur.fetchall()
                return rows
        return _select_table_many_data

    def select_table_one_data(self, func : object)->object:
        botPatch = self.path
        def _select_table_one_data(self : object = None, dados = {}):
            with connect(botPatch) as db:
                db.row_factory = dict_factory
                cur = db.cursor()
                script = func(self, dados)
                cur.execute(script, dados)
                rows = cur.fetchone()
                return rows
        return _select_table_one_data
