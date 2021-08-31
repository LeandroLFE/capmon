'''
Requer: {
    "nome_canal" : str,
    "aventureiro_capcoins" : int,
    "aventureiro_nome" : str,
}
'''

update_capcoins = lambda dados : f"""
    UPDATE aventureiros_{dados["canal_id"]} 
    SET capcoins = :aventureiro_capcoins
    WHERE Nome = :aventureiro_nome
"""