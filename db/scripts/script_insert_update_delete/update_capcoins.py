'''
Requer: {
    "canal_id" : str,
    "capcoins" : int,
    "aventureiro_id" : str,
}
'''

script_update_capcoins = lambda dados : f"""
    UPDATE aventureiros_{dados["canal_id"]} 
    SET capcoins = :capcoins
    WHERE aventureiro_id = :aventureiro_id
"""