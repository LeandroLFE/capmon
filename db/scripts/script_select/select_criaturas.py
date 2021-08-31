select_criatura_aleatoria = lambda idioma : f"""
    SELECT criaturas.num, criaturas.tipo, criaturas.Nome, criaturas.CP_Min, criaturas.CP_Max, 
    atr1.Nome_{idioma} AS "Atributo1", atr1.Id as "Ref1", 
    atr2.Nome_{idioma} AS "Atributo2", atr2.Id as "Ref2", 
    criaturas.chance_especial, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.Custo, criaturas.evolucao, criaturas.CP_limite, criaturas.custo 
    FROM criaturas 
    INNER JOIN atributos as atr1 
    ON criaturas.atributo1 = atr1.Id 
    AND criaturas.tipo = atr1.tipo 
    LEFT JOIN atributos AS atr2 
    ON criaturas.atributo2 = atr2.Id 
    AND criaturas.tipo = atr2.tipo 
    WHERE criaturas.forma = 1 
    AND criaturas.Custo <> 5 
    ORDER BY RAND() 
    LIMIT 1
"""

select_criatura_aleatoria_lendaria = lambda idioma : f"""
    SELECT criaturas.num, criaturas.tipo, criaturas.Nome, criaturas.CP_Min, criaturas.CP_Max, 
    atr1.Nome_{idioma} AS "Atributo1", atr1.Id as "Ref1", 
    atr2.Nome_{idioma} AS "Atributo2", atr2.Id as "Ref2", 
    criaturas.chance_especial, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.Custo, criaturas.evolucao, criaturas.CP_limite, criaturas.custo 
    FROM criaturas 
    INNER JOIN atributos as atr1 
    ON criaturas.atributo1 = atr1.Id 
    AND criaturas.tipo = atr1.tipo 
    LEFT JOIN atributos AS atr2 
    ON criaturas.atributo2 = atr2.Id 
    AND criaturas.tipo = atr2.tipo 
    WHERE criaturas.forma = 1 
    AND criaturas.Custo = 5 
    ORDER BY RAND() 
    LIMIT 1;
"""

# Requer nome = { "nome": "Nome_da_criatura"}
select_criatura_especifica = lambda idioma : f"""
    SELECT criaturas.num, criaturas.tipo, criaturas.Nome, criaturas.CP_Min, criaturas.CP_Max, 
    atr1.Nome_{idioma} AS "Atributo1", atr1.Id as "Ref1", 
    atr2.Nome_{idioma} AS "Atributo2", atr2.Id as "Ref2", 
    criaturas.chance_especial, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.Custo, criaturas.evolucao, criaturas.CP_limite 
    FROM criaturas 
    INNER JOIN atributos as atr1 
    ON criaturas.atributo1 = atr1.Id 
    AND criaturas.tipo = atr1.tipo 
    LEFT JOIN atributos AS atr2 
    ON criaturas.atributo2 = atr2.Id 
    AND criaturas.tipo = atr2.tipo 
    WHERE criaturas.forma = 1 
    AND criaturas.Nome = :nome
    LIMIT 1;
"""

# Requer custo e ref = { "custo": custo da criatura sorteado, "ref": "Ref do atributo sorteado"}
select_criaturas_atributo = lambda idioma : f"""
    SELECT criaturas.num, criaturas.tipo, criaturas.Nome, criaturas.CP_Min, criaturas.CP_Max,
    atr1.Nome_{idioma} AS "Atributo1", atr1.Id as "Ref1", 
    atr2.Nome_{idioma} AS "Atributo2", atr2.Id as "Ref2",
    criaturas.chance_especial, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.Custo, criaturas.evolucao, criaturas.CP_limite, criaturas.custo 
    FROM criaturas 
    INNER JOIN atributos as atr1 
    ON criaturas.atributo1 = atr1.Id 
    AND criaturas.tipo = atr1.tipo 
    LEFT JOIN atributos AS atr2 
    ON criaturas.atributo2 = atr2.Id 
    AND criaturas.tipo = atr2.tipo 
    WHERE criaturas.forma = 1 
    AND criaturas.Custo = :custo
    AND ( 
    atr1.Id = :ref
    OR atr2.Id = :ref
    ) 
    ORDER BY RAND() 
    LIMIT 10;
""" 