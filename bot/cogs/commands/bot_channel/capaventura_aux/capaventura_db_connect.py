from db.connect.instanciaAtualDB import atualDB
from db.scripts.script_select.select_canais import select_verifica_canal, select_canais_ativos
from db.scripts.script_select.select_aventureiros import select_aventureiro_nome, select_aventureiro_id
from db.scripts.script_create_drop.create_tables import create_aventureiros_canal, create_buddies_canal, create_capturados_canal, create_capboard_dados_canal, create_itens_obtidos_canal
from db.scripts.script_create_drop.drop_tables import drop_table_aventureiros_canal, drop_table_buddies_canal, drop_table_capturados_canal, drop_capboard_dados_canal, drop_itens_obtidos_canal
from db.scripts.script_insert_update_delete.update_insert_canais import script_insert_canais, script_update_canais 
from db.scripts.script_insert_update_delete.insert_aventureiros import script_insert_aventureiros
from db.scripts.script_select.select_idiomas import script_select_todos_idiomas, script_select_idioma_por_nome
from db.scripts.script_insert_update_delete.insert_tipo_itens import script_insert_tipo_itens
from db.scripts.script_select.select_parametros_canal import select_parametros_aventureiros_novo_canal

class Capaventura_DB_Connect():

    def __init__(self) -> None:
        pass

    @atualDB.select_table_many_data
    async def consulta_todos_idiomas(self, dados ={}):
        _select_idiomas = script_select_todos_idiomas(dados)
        return _select_idiomas 

    @atualDB.select_table_one_data
    async def consulta_idioma_por_nome(self, dados ={}):
        _select_idioma_por_nome = script_select_idioma_por_nome(dados)
        return _select_idioma_por_nome 

    @atualDB.select_table_one_data
    async def consulta_parametros_aventureiros_novo_canal(self, dados ={}):
        _select_parametros_aventureiros_novo_canal = select_parametros_aventureiros_novo_canal()
        return _select_parametros_aventureiros_novo_canal

    @atualDB.select_table_one_data
    async def consulta_aventureiro_por_nome(self, dados ={}):
        _select_aventureiro_por_nome = select_aventureiro_nome(dados)
        return _select_aventureiro_por_nome 

    @atualDB.select_table_one_data
    async def consulta_aventureiro_por_id(self, dados ={}):
        _select_aventureiro_por_id = select_aventureiro_id(dados)
        return _select_aventureiro_por_id 

    @atualDB.select_table_many_data
    async def consulta_canais_ativos_existentes(self, dados ={}):
        _consulta_canais_existentes = select_canais_ativos(dados)
        return _consulta_canais_existentes 

    @atualDB.select_table_one_data
    async def consulta_canal_dado_um_id(self, dados ={}):
        _consulta_canal_dado_um_id = select_verifica_canal(dados)
        return _consulta_canal_dado_um_id

    @atualDB.update_table
    async def update_canais(self, dados ={}):
        _update_canais = script_update_canais(dados)
        return _update_canais

    @atualDB.insert_table_one_line
    async def insert_canais(self, dados ={}):
        _insert_canais = script_insert_canais(dados)
        return _insert_canais

    @atualDB.insert_table_many_lines
    async def insert_tipo_itens(self, dados ={}):
        _insert_tipo_itens = script_insert_tipo_itens(dados)
        return _insert_tipo_itens

    @atualDB.insert_table_one_line
    async def insert_aventureiro(self, dados={}):
        _insert_aventureiros = script_insert_aventureiros(dados)
        return _insert_aventureiros

    @atualDB.create_or_drop_table
    async def create_tables_with_underline_adventurer_name(self, dados={}):
        _create_tables = create_aventureiros_canal(dados) + create_buddies_canal(dados) + create_capturados_canal(dados) + create_itens_obtidos_canal(dados) + create_capboard_dados_canal(dados)
        return _create_tables

    @atualDB.create_or_drop_table
    async def drop_tables_with_underline_adventurer_name(self, dados={}):
        _drop_tables = drop_capboard_dados_canal(dados) + drop_itens_obtidos_canal(dados) + drop_table_capturados_canal(dados) + drop_table_buddies_canal(dados) + drop_table_aventureiros_canal(dados)
        return _drop_tables