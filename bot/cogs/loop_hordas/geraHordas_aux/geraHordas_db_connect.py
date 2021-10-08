from db.connect.instanciaAtualDB import atualDB
from db.scripts.script_select.select_criaturas import select_criatura_aleatoria, select_criatura_especifica, select_criaturas_atributo, select_criatura_aleatoria_lendaria
from db.scripts.script_select.select_horda_ativa_canal import select_horda_ativa_canal
from db.scripts.script_insert_update_delete.insert_update_hordas_canal import script_update_table_hordas_horda_ativa_canal, script_update_table_hordas_tipo_horda_canal
from db.scripts.script_insert_update_delete.insert_update_tipo_hordas_canal import script_update_table_tipo_hordas_reset_percent_atual, script_update_table_tipo_hordas_elemental_canal, script_update_table_tipo_hordas_capraid_canal, script_update_table_tipo_hordas_horda_especifica_canal
from db.scripts.script_select.select_parametros_canal import select_parametros_hordas_canal, select_parametros_aventureiros_canal
from db.scripts.script_select.select_idiomas import script_select_idioma_por_canal_id
from db.scripts.script_select.select_atributos import select_all_ref_atributos, select_atributos_ref
from db.scripts.script_select.select_custos import select_all_ref_custos
from db.scripts.script_insert_update_delete.insert_update_aventureiros import script_insert_update_aventureiros_canal
from db.scripts.script_insert_update_delete.insert_update_capturados import script_insert_update_capturados
from db.scripts.script_insert_update_delete.update_aventureiros import script_reset_cont_sequencia_outros_aventureiros


class Gera_Hordas_DB_Connect():

    def __init__(self) -> None:
        pass

    @atualDB.select_table_one_data
    async def seleciona_criatura_aleatoria(self, dados = {}):
        _seleciona_criatura_aleatoria = select_criatura_aleatoria(dados)
        return _seleciona_criatura_aleatoria

    @atualDB.select_table_one_data
    async def seleciona_criatura_especifica(self, dados = {}):
        _seleciona_criatura_especifica = select_criatura_especifica(dados)
        return _seleciona_criatura_especifica

    @atualDB.select_table_many_data
    async def seleciona_todos_atributos(self, dados = {}):
        _seleciona_todos_atributos = select_all_ref_atributos(dados)
        return _seleciona_todos_atributos

    @atualDB.select_table_one_data
    async def seleciona_atributo_por_ref(self, dados = {}):
        _seleciona_atributo_por_ref = select_atributos_ref(dados)
        return _seleciona_atributo_por_ref

    @atualDB.select_table_many_data
    async def seleciona_todos_custos(self, dados = {}):
        _seleciona_todos_custos = select_all_ref_custos(dados)
        return _seleciona_todos_custos

    @atualDB.select_table_many_data
    async def seleciona_criaturas_atributo(self, dados = {}):
        _seleciona_criaturas_atributo = select_criaturas_atributo(dados)
        return _seleciona_criaturas_atributo

    @atualDB.select_table_one_data
    async def seleciona_criatura_aleatoria_lendaria(self, dados = {}):
        _seleciona_criatura_aleatoria_lendaria = select_criatura_aleatoria_lendaria(dados)
        return _seleciona_criatura_aleatoria_lendaria

    @atualDB.select_table_one_data
    async def consulta_parametros_hordas_canal(self, dados ={}):
        _consulta_parametros_hordas_canal = select_parametros_hordas_canal(dados)
        return _consulta_parametros_hordas_canal

    @atualDB.select_table_one_data
    async def consulta_parametros_aventureiros_canal(self, dados = {}):
        _consulta_parametros_aventureiros_canal = select_parametros_aventureiros_canal(dados)
        return _consulta_parametros_aventureiros_canal

    @atualDB.select_table_one_data
    async def seleciona_horda_ativa_canal(self, dados = {}):
        _seleciona_horda_ativa_canal = select_horda_ativa_canal(dados)
        return _seleciona_horda_ativa_canal

    @atualDB.select_table_one_data
    async def consulta_idioma_por_canal_id(self, dados ={}):
        _select_idioma_por_canal_id = script_select_idioma_por_canal_id(dados)
        return _select_idioma_por_canal_id

    @atualDB.update_table
    async def update_tipo_horda_ativa(self, dados = {}):
        _update_tipo_horda_ativa = script_update_table_hordas_tipo_horda_canal(dados)
        return _update_tipo_horda_ativa

    @atualDB.update_table
    async def update_ativa_horda(self, dados = {}):
        _update_ativa_horda = script_update_table_hordas_horda_ativa_canal(dados)
        return _update_ativa_horda

    @atualDB.update_table
    async def update_tipo_hordas_reset(self, dados = {}):
        _update_tipo_hordas_reset = script_update_table_tipo_hordas_reset_percent_atual(dados)
        return _update_tipo_hordas_reset

    @atualDB.update_table
    async def update_tipo_hordas_elemental(self, dados = {}):
        _update_tipo_hordas_elemental = script_update_table_tipo_hordas_elemental_canal(dados)
        return _update_tipo_hordas_elemental

    @atualDB.update_table
    async def update_tipo_hordas_capraid(self, dados = {}):
        _update_tipo_hordas_capraid = script_update_table_tipo_hordas_capraid_canal(dados)
        return _update_tipo_hordas_capraid

    @atualDB.update_table
    async def update_tipo_hordas_horda_especifica(self, dados = {}):
        _update_tipo_hordas_horda_especifica = script_update_table_tipo_hordas_horda_especifica_canal(dados)
        return _update_tipo_hordas_horda_especifica    

    @atualDB.insert_table_many_lines
    async def insert_update_aventureiros(self, dados = {}):
        _insert_update_aventureiros = script_insert_update_aventureiros_canal(dados)
        return _insert_update_aventureiros

    @atualDB.update_table
    async def reset_cont_sequencia_outros_aventureiros(self, dados = {}):
        _reset_cont_sequencia_outros_aventureiros = script_reset_cont_sequencia_outros_aventureiros(dados)
        return _reset_cont_sequencia_outros_aventureiros

    @atualDB.insert_table_many_lines
    async def insert_update_capturados(self, dados = {}):
        _insert_update_capturados = script_insert_update_capturados(dados)
        return _insert_update_capturados