"""
Capshop = 1
Capraid = 2

Requer:{
    "id_item" : int,
}

"""

script_delete_itens_sem_qtde_capshop = lambda dados : f"""
    DELETE FROM Itens_obtidos_{dados["canal_id"]}
    WHERE tipo_item = 1
    AND id_item = :id_item
    And qtde = 0
""" 

script_delete_itens_expirados = lambda dados : f"""
    DELETE FROM Itens_obtidos_{dados["canal_id"]}
    WHERE data_expiracao <= date('Now', 'Localtime')
"""