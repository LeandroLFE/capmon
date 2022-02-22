from db.connect.instanciaAtualDB import atualDB
from db.scripts.script_select.select_aventureiros import script_select_aventureiro_id
from db.scripts.script_insert_update_delete.insert_aventureiros import script_insert_aventureiros
from db.scripts.script_select.select_tipos import select_tipos
from db.scripts.script_select.select_atributos import select_all_ref_atributos, select_atributos_tipo
from db.scripts.script_select.select_custos import select_all_ref_custos
from db.scripts.script_select.select_especiais import select_all_ref_especiais
from db.scripts.script_select.select_capturados_individuais import select_capturados_atributo_individuais, select_capturados_tipo_individuais, select_capturados_especial_individuais, select_capturados_raridade_individuais
from db.scripts.script_select.select_parametros_canal import select_parametros_gerais_canal

class Capmon_DB_Connect():

    def __init__(self) -> None:
        pass

    @atualDB.select_table_one_data
    async def consulta_aventureiro(self, dados = {}):
        _consulta_aventureiro = script_select_aventureiro_id(dados)
        return _consulta_aventureiro

    @atualDB.insert_table_one_line
    async def insert_aventureiro(self, dados={}):
        _insert_aventureiros = script_insert_aventureiros(dados)
        return _insert_aventureiros

    @atualDB.select_table_many_data
    async def consulta_tipos_disponiveis(self, dados = {}):
        _consulta_tipos_disponiveis = select_tipos(dados)
        return _consulta_tipos_disponiveis

    @atualDB.select_table_many_data
    async def consulta_atributos_disponiveis(self, dados = {}):
        _consulta_atributos_disponiveis = select_all_ref_atributos(dados)
        return _consulta_atributos_disponiveis
    
    @atualDB.select_table_many_data
    async def consulta_custos_disponiveis(self, dados = {}):
        _consulta_custos_disponiveis = select_all_ref_custos(dados)
        return _consulta_custos_disponiveis

    @atualDB.select_table_many_data
    async def consulta_especiais_disponiveis(self, dados = {}):
        _consulta_especiais_disponiveis = select_all_ref_especiais(dados)
        return _consulta_especiais_disponiveis

    @atualDB.select_table_many_data
    async def seleciona_capturados_atributo(self, dados = {}):
        _seleciona_capturados_atributo = select_capturados_atributo_individuais(dados)
        return _seleciona_capturados_atributo

    @atualDB.select_table_many_data
    async def seleciona_capturados_tipo(self, dados = {}):
        _seleciona_capturados_tipo = select_capturados_tipo_individuais(dados)
        return _seleciona_capturados_tipo
    
    @atualDB.select_table_many_data
    async def seleciona_capturados_raridade(self, dados = {}):
        _seleciona_capturados_raridade = select_capturados_raridade_individuais(dados)
        return _seleciona_capturados_raridade
    
    @atualDB.select_table_many_data
    async def seleciona_capturados_especial(self, dados = {}):
        _seleciona_capturados_especial = select_capturados_especial_individuais(dados)
        return _seleciona_capturados_especial

    @atualDB.select_table_one_data
    async def consulta_parametros_gerais(self, dados = {}):
        _consulta_parametros_gerais = select_parametros_gerais_canal(dados)
        return _consulta_parametros_gerais