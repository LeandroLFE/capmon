from db.connect.instanciaAtualDB import atualDB
from db.scripts.script_select.select_aventureiros import script_select_aventureiro_id
from db.scripts.script_insert_update_delete.insert_update_itens_obtidos import script_insert_update_itens_obtidos
from db.scripts.script_insert_update_delete.update_capcoins import script_update_capcoins

class Whispers_DB_Connect():

    def __init__(self) -> None:
        pass

    @atualDB.select_table_one_data
    async def consulta_aventureiro(self, dados = {}):
        _consulta_aventureiro = script_select_aventureiro_id(dados)
        return _consulta_aventureiro

    @atualDB.insert_table_one_line
    async def insert_update_itens_obtidos(self, dados = {}):
        _insert_update_itens_obtidos = script_insert_update_itens_obtidos(dados)
        return _insert_update_itens_obtidos

    @atualDB.update_table
    async def update_capcoins_aventureiro(self, dados={}):
        _update_capcoins_aventureiro = script_update_capcoins(dados)
        return _update_capcoins_aventureiro