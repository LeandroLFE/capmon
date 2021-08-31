# Requer nome_aventureiro = {"nome_aventureiro" : str}
select_capcoins = lambda dados : f"""
    Select capcoins
    FROM aventureiros_{dados["nome_canal"]} AS aventureiros 
    Where Nome = :nome_aventureiro 
"""