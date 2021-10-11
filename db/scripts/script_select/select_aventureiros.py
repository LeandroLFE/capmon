script_select_aventureiros = lambda dados = {}: f"""
    Select DISTINCT aventureiro_id, nome, capcoins, cont_hordas, cont_sequencia, bonus 
    FROM aventureiros_{dados["canal_id"]} AS aventureiros 
    ORDER BY aventureiro_id 
"""

# Requer nome_aventureiro = {"canal_id" : str, "nome_aventureiro": str}
script_select_aventureiro_nome = lambda dados = {}: f"""
    Select Aventureiros.aventureiro_id, Aventureiros.nome as nome_aventureiro, 
        capcoins, cont_hordas_atual, cont_sequencia_atual
    FROM aventureiros_{dados["canal_id"]} AS aventureiros 
    WHERE LOWER(nome_Aventureiro) = LOWER(:aventureiro_nome)
"""

# Requer nome_aventureiro = {"canal_id" : str, "aventureiro_id": str}
script_select_aventureiro_id = lambda dados = {}: f"""
    Select Aventureiros.aventureiro_id, Aventureiros.nome as aventureiro_nome, 
        capcoins, cont_hordas_atual, cont_sequencia_atual
    FROM aventureiros_{dados["canal_id"]} AS aventureiros 
    WHERE Aventureiros.aventureiro_id = :aventureiro_id
"""
