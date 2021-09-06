from db.connect.instanciaAtualDB import atualDB
from db.scripts.script_select.select_mensagens import select_ultima_msg
from db.scripts.script_select.select_canais import select_canal_id_por_nome
from db.scripts.script_insert_update_delete.insert_update_mensagens import script_update_msg, script_insert_msg

class Envia_MSG_Chat_DB_Connect():

    def __init__(self) -> None:
        pass

    @atualDB.select_table_one_data
    async def consulta_ultima_msg(self, dados = {}):
        _select_ultima_msg = select_ultima_msg(dados)
        return _select_ultima_msg

    @atualDB.select_table_one_data
    async def consulta_channel_id(self, dados = {}):
        _select_channel_id = select_canal_id_por_nome(dados)
        return _select_channel_id

    @atualDB.update_table
    async def update_ultima_msg(self, dados = {}):
        _update_ultima_msg = script_update_msg(dados)
        return _update_ultima_msg

    @atualDB.insert_table_one_line
    async def insert_ultima_msg(self, dados = {}):
        _insert_ultima_msg = script_insert_msg(dados)
        return _insert_ultima_msg