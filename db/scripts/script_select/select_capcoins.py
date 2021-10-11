# Requer {"canal_id" : str, "aventureiro_id" : str}
select_capcoins = lambda dados : f"""
    Select capcoins
    FROM aventureiros_{dados["canal_id"]} AS aventureiros 
    Where aventureiro_id = :aventureiro_id 
"""