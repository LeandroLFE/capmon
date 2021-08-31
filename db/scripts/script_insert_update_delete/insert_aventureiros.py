'''
Requer: {
    "canal_id" : str,
    "aventureiro_id": str,
    "aventureiro_nome": str,
    "capcoins_iniciais" : str
}

'''

script_insert_aventureiros = lambda dados = {} : f"""
    INSERT INTO Aventureiros_{dados["canal_id"]} (aventureiro_id, nome, capcoins) 
    VALUES (:aventureiro_id, :aventureiro_nome, :capcoins_iniciais);
"""