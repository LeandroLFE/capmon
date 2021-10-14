from db.connect.instanciaAtualDB import atualDB
from db.scripts.script_select.select_aventureiros import script_select_aventureiro_id
from db.scripts.script_select.select_vantagens_subs_canal import select_vantagens_subs_canal
from db.scripts.script_select.select_itens_obtidos import select_itens_obtidos_aventureiro_canal
from db.scripts.script_select.select_itens_capshop import script_select_itens_capshop
from db.scripts.script_insert_update_delete.insert_aventureiros import script_insert_aventureiros

class Capshop_DB_Connect():

    def __init__(self) -> None:
        pass

    @atualDB.select_table_one_data
    async def consulta_aventureiro(self, dados = {}):
        _consulta_aventureiro = script_select_aventureiro_id(dados)
        return _consulta_aventureiro

    @atualDB.select_table_one_data
    async def consulta_vantagens_subs_canal(self, dados={}):
        _select_vantagens_subs_canal = select_vantagens_subs_canal(dados)
        return _select_vantagens_subs_canal 

    @atualDB.select_table_many_data
    async def consulta_itens_obtidos(self, dados={}):
        _consulta_itens_obtidos = select_itens_obtidos_aventureiro_canal(dados)
        return _consulta_itens_obtidos

    @atualDB.select_table_many_data
    async def consulta_itens_capshop(self, dados={}):
        _consulta_itens_capshop = script_select_itens_capshop(dados)
        return _consulta_itens_capshop

    @atualDB.insert_table_one_line
    async def insert_aventureiro(self, dados={}):
        _insert_aventureiros = script_insert_aventureiros(dados)
        return _insert_aventureiros