# Requer num e tipo = {"num": int, "tipo": int}
select_atributos_criatura = lambda dados = {} : """
    Select atributo1, atributo 2 
    FROM criaturas 
    WHERE Num = :num 
    AND tipo = :tipo ;
"""

select_all_ref_atributos = lambda dados = {} : """
    SELECT Distinct ref 
    FROM atributos
"""
# Requer tipo e ref = {"tipo": int, "ref":int}
select_atributos_ref = lambda dados = {} : """
    SELECT Atributos.nome 
    FROM Atributos 
    INNER JOIN Idiomas
    ON Atributos.idioma = Idiomas.id
    INNER JOIN Tipos
    ON Atributos.tipo = Tipos.id
    WHERE Tipos.nome = :nome_tipo
    AND Idiomas.nome = :nome_idioma
    AND ref = :ref_atributo 
"""
# Requer tipo = {"tipo": int}
select_atributos_tipo = lambda dados = {} : """
    SELECT Distinct id, Nome, Idioma, tipo, Ref 
    FROM atributos 
    WHERE tipo = :tipo
"""

