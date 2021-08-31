# Requer num e tipo = {"num": int, "tipo": int}
select_atributos_criatura = lambda dados = {} : """
    Select atributo1, atributo 2 
    FROM criaturas 
    WHERE Num = :num 
    AND tipo = :tipo ;
"""

select_all_atributos = lambda dados = {} : """
    SELECT Distinct id, Nome, Idioma, tipo, Ref 
    FROM atributos
"""
# Requer tipo e ref = {"tipo": int, "ref":int}
select_atributos_id = lambda dados = {} : """
    SELECT Distinct id, Nome, Idioma, tipo, Ref 
    FROM atributos 
    WHERE tipo = :tipo
    AND ref = :ref 
"""
# Requer tipo = {"tipo": int}
select_atributos_tipo = lambda dados = {} : """
    SELECT Distinct id, Nome, Idioma, tipo, Ref 
    FROM atributos 
    WHERE tipo = :tipo
"""

