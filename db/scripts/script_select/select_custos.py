select_all_ref_custos = lambda dados = {}: """
    SELECT Custos.nome, Custos.ref, Idiomas.nome as nome_idioma 
    FROM Custos
    INNER JOIN Idiomas
    ON Custos.idioma = Idiomas.id
    ORDER BY Custos.ref DESC
"""