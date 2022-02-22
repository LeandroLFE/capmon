select_all_ref_especiais = lambda dados = {}: """
    SELECT Especiais.nome, Especiais.ref, Idiomas.nome as nome_idioma 
    FROM Especiais
    INNER JOIN Idiomas
    ON Especiais.idioma = Idiomas.id
"""