from db.connect.instanciaAtualDB import atualDB
from db.scripts.script_select.select_parametros_canal import select_parametros_hordas_canal

class Event_Join_DB_Connect():

    def __init__(self) -> None:
        pass

    @atualDB.select_table_one_data
    async def consulta_parametros_hordas_canal(self, dados ={}):
        _consulta_parametros_hordas_canal = select_parametros_hordas_canal()
        return _consulta_parametros_hordas_canal