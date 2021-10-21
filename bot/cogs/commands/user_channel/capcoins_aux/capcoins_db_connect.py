from db.connect.instanciaAtualDB import atualDB
from db.scripts.script_select.select_capcoins import select_capcoins
from db.scripts.script_select.select_itens_obtidos import select_itens_obtidos_capshop_aventureiro_canal, select_itens_obtidos_capraid_aventureiro_canal
from db.scripts.script_insert_update_delete.insert_aventureiros import script_insert_aventureiros
from db.scripts.script_insert_update_delete.update_capcoins import script_update_capcoins
from db.scripts.script_select.select_aventureiros import script_select_aventureiro_nome

class Capcoins_DB_Connect():

    def __init__(self) -> None:
        pass

    @atualDB.select_table_one_data
    async def consulta_capcoins(self, dados = {}):
        _consulta_capcoins = select_capcoins(dados)
        return _consulta_capcoins

    @atualDB.select_table_many_data
    async def consulta_itens_obtidos_capshop(self, dados={}):
        _consulta_itens_obtidos = select_itens_obtidos_capshop_aventureiro_canal(dados)
        return _consulta_itens_obtidos

    @atualDB.select_table_many_data
    async def consulta_itens_obtidos_capraid(self, dados={}):
        _consulta_itens_obtidos = select_itens_obtidos_capraid_aventureiro_canal(dados)
        return _consulta_itens_obtidos

    @atualDB.select_table_one_data
    async def consulta_aventureiro(self, dados = {}):
        _consulta_aventureiro = script_select_aventureiro_nome(dados)
        return _consulta_aventureiro

    @atualDB.insert_table_one_line
    async def insert_aventureiro(self, dados={}):
        _insert_aventureiros = script_insert_aventureiros(dados)
        return _insert_aventureiros

    @atualDB.update_table
    async def update_capcoins_aventureiro(self, dados={}):
        _update_capcoins_aventureiro = script_update_capcoins(dados)
        return _update_capcoins_aventureiro