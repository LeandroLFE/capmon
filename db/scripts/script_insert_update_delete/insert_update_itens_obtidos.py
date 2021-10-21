'''
Requer: {
    "canal_id" : str,
    "aventureiro_id": str,
    "tipo_item" : int,
    "id_item" : int,
    "qtde" : int
}

'''

script_insert_update_itens_obtidos = lambda dados = {}  : f"""
    INSERT INTO Itens_obtidos_{dados["canal_id"]} (aventureiro_id, tipo_item, id_item, qtde, data_expiracao) 
    VALUES (:aventureiro_id, :tipo_item, :id_item, :qtde,  date('now', 'LocalTime', '+8 day')) 
    ON CONFLICT(aventureiro_id, tipo_item, id_item) DO 
    UPDATE  
    SET qtde = qtde + :qtde,
    data_expiracao = date('Now', 'LocalTime', '+8 Day')
    WHERE aventureiro_id = :aventureiro_id
"""

'''
Requer: {
    "canal_id" : str,
    "aventureiro_id" : str,
    "tipo_item" : int,
    "id_item" : int,
    "qtde_utilizada" : int
}

'''

script_utiliza_item = lambda dados = {} : f"""
    UPDATE Itens_obtidos_{dados["canal_id"]} 
    SET qtde = qtde - :qtde_utilizada
    WHERE aventureiro_id = :aventureiro_id
    AND tipo_item = :tipo_item
    AND id_item = :id_item
"""

