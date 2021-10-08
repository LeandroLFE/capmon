'''
Requer: {
    "canal_id" : str,
    "aventureiro_id": str,
    "nome" : str,
    "capcoins" : long,
    "cont_hordas_atual" : int,
    "cont_sequencia_atual" : int,
}

'''

script_insert_update_aventureiros_canal = lambda dados = {}  : f"""
    INSERT INTO Aventureiros_{dados["canal_id"]} (aventureiro_id, nome, capcoins) 
    VALUES (:aventureiro_id, :nome, :capcoins) 
    ON CONFLICT(aventureiro_id) DO 
    UPDATE  
    SET nome = :nome , 
    capcoins = :capcoins ,
    cont_hordas_atual = :cont_hordas_atual ,
    cont_sequencia_atual = :cont_sequencia_atual 
    WHERE aventureiro_id = :aventureiro_id
"""