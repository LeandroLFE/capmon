select_aventureiros = lambda dados = {} : f"""
    Select DISTINCT aventureiro_id, nome, capcoins, cont_hordas, cont_sequencia, bonus 
    FROM aventureiros_{dados["canal_id"]} AS aventureiros 
    ORDER BY aventureiro_Id 
"""

# Requer nome_aventureiro = {"nome_aventureiro": str} 
select_aventureiro_nome = lambda dados = {} : f"""
    Select DISTINCT Aventureiros.aventureiro_id, Aventureiros.nome as nome_aventureiro, 
        capcoins, cont_Hordas, cont_Sequencia, Idiomas.nome as nome_idioma
    FROM aventureiros_{dados["canal_id"]} AS aventureiros 
    INNER JOIN ( Canais
        INNER JOIN Idiomas
        ON Canais.idioma = Idiomas.id )
    ON Aventureiros.aventureiro_id = Canais.aventureiro_id
    WHERE nome_Aventureiro = :nome_aventureiro
    ORDER BY Aventureiros.nome 
"""

# Requer nome_aventureiro = {"aventureiro_id": str} 
select_aventureiro_id = lambda dados = {} : f"""
    Select DISTINCT Aventureiros.aventureiro_id, Aventureiros.nome as nome_aventureiro, 
        capcoins, cont_Hordas, cont_Sequencia, Idiomas.nome as nome_idioma
    FROM aventureiros_{dados["canal_id"]} AS aventureiros 
    INNER JOIN ( Canais
        INNER JOIN Idiomas
        ON Canais.idioma = Idiomas.id )
    ON Aventureiros.aventureiro_id = Canais.aventureiro_id
    WHERE Aventureiros.aventureiro_id = :aventureiro_id
    ORDER BY Aventureiros.aventureiro_id 
"""
