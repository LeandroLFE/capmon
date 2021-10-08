'''
Requer {
    "nome_idioma" : str
}
'''

select_criatura_aleatoria = lambda dados = {} : f"""
    SELECT Criaturas.num, Tipos.nome as nome_tipo, Criaturas.Nome, Criaturas.forma,
    Criaturas.linha_evolutiva,
    Criaturas.cp_min, Criaturas.cp_max, 
    Atr1.nome AS "nome_atributo1",
    Atr2.nome AS "nome_atributo2",
    Criaturas.chance_especial,  
    Criaturas.custo, 
    Criaturas.evolucao, 
    Criaturas.cp_limite, 
    Criaturas.evolui 
    FROM Criaturas 
    INNER JOIN Tipos
    ON Criaturas.tipo = Tipos.id
    INNER JOIN 
    (
    SELECT Atributos.nome, Atributos.ref, Atributos.tipo, Idiomas.nome as nome_idioma_atr1
    FROM Atributos 
    INNER JOIN Idiomas 
    ON Atributos.idioma = Idiomas.id
    ) AS Atr1
    ON Criaturas.atributo1 = Atr1.ref 
    AND Criaturas.tipo = Atr1.tipo 
    LEFT JOIN (
    SELECT Atributos.nome, Atributos.ref, Atributos.tipo, Idiomas.nome as nome_idioma_atr2
    FROM Atributos 
    INNER JOIN Idiomas 
    ON Atributos.idioma = Idiomas.id
    ) AS Atr2
    ON criaturas.atributo2 = Atr2.ref 
    AND criaturas.tipo = Atr2.tipo 
    WHERE Criaturas.forma = 1 
    AND Criaturas.custo <> 5 
    AND Atr1.nome_idioma_atr1 = :nome_idioma
    AND Atr2.nome_idioma_atr2 = :nome_idioma
    ORDER BY RANDOM() 
    LIMIT 1
"""

select_criatura_aleatoria_lendaria = lambda idioma : f"""
    SELECT Criaturas.num, Tipos.nome as nome_tipo, Criaturas.Nome, Criaturas.forma,
    Criaturas.linha_evolutiva,
    Criaturas.cp_min, Criaturas.cp_max, 
    Atr1.nome AS "nome_atributo1",
    Atr2.nome AS "nome_atributo2",
    Criaturas.chance_especial,  
    Criaturas.custo, 
    Criaturas.evolucao, 
    Criaturas.cp_limite, 
    Criaturas.evolui 
    FROM Criaturas 
    INNER JOIN Tipos
    ON Criaturas.tipo = Tipos.id
    INNER JOIN 
    (
    SELECT Atributos.nome, Atributos.ref, Atributos.tipo, Idiomas.nome as nome_idioma_atr1
    FROM Atributos 
    INNER JOIN Idiomas 
    ON Atributos.idioma = Idiomas.id
    ) AS Atr1
    ON Criaturas.atributo1 = Atr1.ref 
    AND Criaturas.tipo = Atr1.tipo 
    LEFT JOIN (
    SELECT Atributos.nome, Atributos.ref, Atributos.tipo, Idiomas.nome as nome_idioma_atr2
    FROM Atributos 
    INNER JOIN Idiomas 
    ON Atributos.idioma = Idiomas.id
    ) AS Atr2
    ON criaturas.atributo2 = Atr2.ref 
    AND criaturas.tipo = Atr2.tipo 
    WHERE Criaturas.forma = 1 
    AND Criaturas.custo = 5 
    AND Atr1.nome_idioma_atr1 = :nome_idioma
    AND Atr2.nome_idioma_atr2 = :nome_idioma
    LIMIT 1
"""

# Requer nome = { "id_criatura": "Id_da_criatura"}
select_criatura_especifica = lambda dados : f"""
    SELECT Criaturas.num, Tipos.nome as nome_tipo, Criaturas.Nome, Criaturas.forma,
    Criaturas.linha_evolutiva,
    Criaturas.cp_min, Criaturas.cp_max, 
    Atr1.nome AS "nome_atributo1",
    Atr2.nome AS "nome_atributo2",
    Pc.chance_especial,
    Pc.chance_captura,
    Pc.num_tentativas_caso_zero_ou_negativo,
    Pc.cp_inicial,
    Criaturas.custo, 
    Criaturas.evolucao, 
    Criaturas.cp_limite, 
    Criaturas.evolui 
    FROM Criaturas 
    INNER JOIN Tipos
    ON Criaturas.tipo = Tipos.id
    INNER JOIN Parametros_criaturas as Pc
    ON Criaturas.parametro_criatura = Pc.id 
    INNER JOIN 
    (
    SELECT Atributos.nome, Atributos.ref, Atributos.tipo, Idiomas.nome as nome_idioma_atr1
    FROM Atributos 
    INNER JOIN Idiomas 
    ON Atributos.idioma = Idiomas.id
    ) AS Atr1
    ON Criaturas.atributo1 = Atr1.ref 
    AND Criaturas.tipo = Atr1.tipo 
    LEFT JOIN (
    SELECT Atributos.nome, Atributos.ref, Atributos.tipo, Idiomas.nome as nome_idioma_atr2
    FROM Atributos 
    INNER JOIN Idiomas 
    ON Atributos.idioma = Idiomas.id
    ) AS Atr2
    ON criaturas.atributo2 = Atr2.ref 
    AND criaturas.tipo = Atr2.tipo 
    WHERE Criaturas.num = :num_criatura
    AND Tipos.nome = :nome_tipo
    AND Atr1.nome_idioma_atr1 = :nome_idioma
    AND Atr2.nome_idioma_atr2 = :nome_idioma
    LIMIT 1
"""

# Requer custo e ref = { "custo": custo da criatura sorteado, "ref": "Ref do atributo sorteado"}
select_criaturas_atributo = lambda idioma : f"""
    SELECT Criaturas.num, Tipos.nome as nome_tipo, Criaturas.Nome, Criaturas.forma,
    Criaturas.linha_evolutiva,
    Criaturas.cp_min, Criaturas.cp_max, 
    Atr1.nome AS "nome_atributo1",
    Atr2.nome AS "nome_atributo2",
    Criaturas.chance_especial,  
    Criaturas.custo, 
    Criaturas.evolucao, 
    Criaturas.cp_limite, 
    Criaturas.evolui 
    FROM Criaturas 
    INNER JOIN Tipos
    ON Criaturas.tipo = Tipos.id
    INNER JOIN 
    (
    SELECT Atributos.nome, Atributos.ref, Atributos.tipo, Idiomas.nome as nome_idioma_atr1
    FROM Atributos 
    INNER JOIN Idiomas 
    ON Atributos.idioma = Idiomas.id
    ) AS Atr1
    ON Criaturas.atributo1 = Atr1.ref 
    AND Criaturas.tipo = Atr1.tipo 
    LEFT JOIN (
    SELECT Atributos.nome, Atributos.ref, Atributos.tipo, Idiomas.nome as nome_idioma_atr2
    FROM Atributos 
    INNER JOIN Idiomas 
    ON Atributos.idioma = Idiomas.id
    ) AS Atr2
    ON criaturas.atributo2 = Atr2.ref 
    AND criaturas.tipo = Atr2.tipo 
    WHERE Criaturas.forma = 1 
    AND Atr1.nome_idioma_atr1 = :nome_idioma
    AND Atr2.nome_idioma_atr2 = :nome_idioma
    AND (Atr1.ref = :ref_atributo OR Atr2.ref = :ref_atributo)
    AND Criaturas.custo = :custo
    ORDER BY RANDOM() 
    LIMIT 1
""" 