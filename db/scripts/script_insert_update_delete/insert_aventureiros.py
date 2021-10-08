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
    VALUES (:aventureiro_id, :aventureiro_nome, (
        SELECT Pa.capcoins_iniciais
        FROM Parametros_aventureiros as Pa
        INNER JOIN Canais 
        ON Pa.id = Canais.parametros_aventureiros
        WHERE canal_id = :canal_id
     ));
"""