from db.connect.instanciaAtualDB import atualDB
from db.scripts.script_select.select_aventureiros import script_select_aventureiro_id
from db.scripts.script_select.select_capturados_individuais import select_capturados_aventureiro_nome
from db.scripts.script_select.select_parametros_canal import select_parametros_criatura
from db.scripts.script_select.select_vantagens_subs_canal import select_vantagens_subs_canal
from db.scripts.script_select.select_itens_obtidos import script_consulta_uso_item_capshop
from db.scripts.script_insert_update_delete.insert_update_itens_obtidos import script_utiliza_item
from db.scripts.script_insert_update_delete.delete_itens_obtidos import script_delete_itens_sem_qtde_capshop
from db.scripts.script_insert_update_delete.insert_aventureiros import script_insert_aventureiros

class Cap_DB_Connect():

    def __init__(self) -> None:
        pass

    @atualDB.select_table_one_data
    async def consulta_aventureiro(self, dados = {}):
        _consulta_aventureiro = script_select_aventureiro_id(dados)
        return _consulta_aventureiro

    @atualDB.select_table_one_data
    async def consulta_se_ja_tem_capturada(self, dados = {}):
        _consulta_se_ja_tem_capturada = select_capturados_aventureiro_nome(dados)
        return _consulta_se_ja_tem_capturada

    @atualDB.select_table_one_data
    async def consulta_parametros_criatura(self, dados ={}):
        _select_parametros_criatura = select_parametros_criatura(dados)
        return _select_parametros_criatura

    @atualDB.select_table_one_data
    async def consulta_vantagens_subs_canal(self, dados={}):
        _select_vantagens_subs_canal = select_vantagens_subs_canal(dados)
        return _select_vantagens_subs_canal 

    @atualDB.select_table_one_data
    async def consulta_uso_item_capshop(self, dados={}):
        _consulta_uso_item_capshop = script_consulta_uso_item_capshop(dados)
        return _consulta_uso_item_capshop

    @atualDB.update_table
    async def atualiza_item_gasto(self, dados={}):
        _atualiza_item_gasto = script_utiliza_item(dados)
        return _atualiza_item_gasto

    @atualDB.delete_table
    async def deleta_itens_sem_qtde_capshop(self, dados={}):
        _deleta_itens_sem_qtde_capshop = script_delete_itens_sem_qtde_capshop(dados)
        return _deleta_itens_sem_qtde_capshop

    @atualDB.insert_table_one_line
    async def insert_aventureiro(self, dados={}):
        _insert_aventureiros = script_insert_aventureiros(dados)
        return _insert_aventureiros