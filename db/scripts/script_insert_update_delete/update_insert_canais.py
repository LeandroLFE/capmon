'''
 Requer : {
     "nome_idioma": str, 
     "ativo": int (0 ou 1), 
     "nome_canal" : str, 
     "canal_id" : str
} 
'''
script_insert_canais = lambda dados = {} : f"""
    INSERT INTO Canais (Canal_ID, Nome_canal, Idioma, Ativo)
    VALUES (:canal_id, :nome_canal, 
    (
        SELECT ID FROM Idiomas
        WHERE nome = :nome_idioma
    ),  
    :ativo 
    );
"""

'''
 Requer : {
     "nome_idioma": str, 
     "ativo": int (0 ou 1), 
     "nome_canal" : str, 
     "canal_id" : str
} 
'''
script_update_canais = lambda dados = {} : """
    UPDATE canais 
    SET Idioma = (
        SELECT ID FROM Idiomas
        WHERE nome = :nome_idioma
    ), 
        Ativo = :ativo, 
        Nome_canal = :nome_canal 
    WHERE Canal_ID = :canal_id
"""
