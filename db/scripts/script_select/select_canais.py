select_canais_ativos = lambda dados = "" : """
            Select canal_id, nome_canal, Idiomas.nome as idioma, ativo
            FROM canais
            INNER JOIN idiomas
            ON canais.idioma = Idiomas.id
            WHERE Ativo = 1
            ORDER BY Nome_canal
"""

'''
Requer: {
    "nome_canal" : str
}
'''

select_canal_id_por_nome = lambda dados = {} : """
    Select Canal_ID
    FROM canais
    WHERE Nome_canal = :nome_canal 
"""

'''
Requer: {
    "canal_id" : str
}
'''
select_verifica_canal = lambda dados = "" : """
    Select canal_id, nome_canal, Idiomas.nome as nome_idioma, ativo
    FROM Canais
    INNER JOIN Idiomas
    ON Canais.idioma = Idiomas.id
    WHERE canal_id = :canal_id
"""
