# Requer num e tipo = {"num": int, "tipo": int}
select_atributos_criatura = lambda dados = {} : """
    Select atributo1, atributo 2 
    FROM criaturas 
    WHERE Num = :num 
    AND tipo = :tipo ;
"""

select_all_ref_atributos = lambda dados = {} : """
    SELECT Atributos.ref, Atributos.nome, Idiomas.nome as nome_idioma 
    FROM atributos
    INNER JOIN Idiomas
    ON Atributos.idioma = Idiomas.id
"""
# Requer nome_tipo, nome_idioma e ref_atributo = {"nome_tipo": str, "nome_idioma": str, "ref_atributo":int}
select_atributos_ref = lambda dados = {} : """
    SELECT Atributos.nome 
    FROM Atributos 
    INNER JOIN Idiomas
    ON Atributos.idioma = Idiomas.id
    INNER JOIN Tipos
    ON Atributos.tipo = Tipos.id
    WHERE LOWER(Tipos.nome) = LOWER(:nome_tipo)
    AND LOWER(Idiomas.nome) = LOWER(:nome_idioma)
    AND ref = :ref_atributo 
"""
# Requer tipo = {"nome_tipo": str}
select_atributos_tipo = lambda dados = {} : """
    SELECT ref, idioma, nome, tipo
    FROM Atributos
    WHERE LOWER(nome) = LOWER(:nome_tipo)
"""