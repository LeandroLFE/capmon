'''
Requer: {
    "canal_id" : str,
    "aventureiro_nome" : str,
    "aventureiro_capcoins" : int,
    "aventureiro_cont_hordas" : int,
    "aventureiro_cont_sequencia" : int,
    "aventureiro_bonus" : int,
    "aventureiro_id" : str,
}
'''

update_aventureiros = lambda dados = {}  : f"""
    UPDATE Aventureiros_{dados["canal_id"]} 
    SET nome = :aventureiro_nome , 
    capcoins = :aventureiro_capcoins ,
    cont_hordas_atual = :aventureiro_cont_hordas_atual ,
    cont_sequencia_atual = :aventureiro_cont_sequencia_atual 
    WHERE aventureiro_id = :aventureiro_id
"""

'''
Requer: {
    "canal_id" : str,
    "parametros_aventureiro" : int,
    "aventureiro_id" : str,
}
'''

update_aventureiros_parametros = lambda dados = {} : f"""
    UPDATE Aventureiros_{dados["canal_id"]} 
    SET parametros_aventureiro = :parametros_aventureiro
    WHERE aventureiro_id = :aventureiro_id;
"""