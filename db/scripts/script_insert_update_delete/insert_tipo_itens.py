'''
Requer: {
    "canal_id" : str,
    "tipo_item_id": int
}

'''

script_insert_tipo_itens = lambda dados = {} : f"""
    INSERT INTO Tipo_itens (id, canal_id) 
    VALUES (:tipo_item_id, :canal_id);
"""