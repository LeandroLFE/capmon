from db.connect.instanciaAtualDB import atualDB
from db.scripts.script_select.select_canais import select_canais_ativos

class Event_Ready_DB_Connect():

    def __init__(self) -> None:
        pass

    @atualDB.select_table_many_data
    async def consulta_canais_ativos(self, dados = {}):
        _select_channels = select_canais_ativos(dados)
        return _select_channels
