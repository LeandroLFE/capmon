# Requer nome_aventureiro e tipo = {"nome_aventureiro":str, "tipo": int} 
select_capturados_tipo = lambda canal : f"""
    Select COUNT(*) as QTDE_Capturados,  
    Count(CASE WHEN Especial = 1 THEN 1 END) As QTDE_Especial, 
    capturados.tipo 
    FROM ( 
    SELECT nome, aventureiro_index 
    FROM aventureiros_{canal} as aventureiros 
    WHERE aventureiros.nome = :nome_aventureiro
    ) as aventureiros 
    LEFT JOIN 
    ( 
    SELECT capturados.Aventureiro_Index, capturados.ID_Criatura, 
    criaturas.tipo, capturados.especial 
    FROM capturados_{canal} as capturados 
    INNER JOIN criaturas 
    ON capturados.ID_Criatura = criaturas.num 
    ) as capturados 
    ON aventureiros.aventureiro_index = capturados.aventureiro_index 
    GROUP BY capturados.aventureiro_index, capturados.tipo 
    HAVING capturados.tipo = :tipo ; 
"""

# Requer atributo, nome_aventureiro e tipo = {"atributo": int, "nome_aventureiro": str, "tipo": int}
select_capturados_atributo = lambda canal, idioma : f"""
    Select count(*) as QTDE_Capturados, Count(CASE WHEN Especial = 1 THEN 1 END) As QTDE_Especial, 
    (SELECT nome_{idioma} from atributos WHERE id = :atributo as atr 
    FROM ( 
    SELECT capturados.Aventureiro_index, capturados.ID_Criatura, capturados.especial 
    FROM capturados_{canal} AS capturados 
    WHERE aventureiro_index = ( 
    SELECT aventureiro_index 
    FROM aventureiros_{canal} 
    WHERE nome = :nome_aventureiro
    ) ) as capturados 
    INNER JOIN ( 
    SELECT criaturas.num, criaturas.nome, 
    (CASE WHEN atributo1 = :atributo THEN atributo1 
    ELSE (CASE WHEN atributo2 = :atributo THEN atributo2 
    ELSE NULL END ) END) AS Atributo 
    FROM criaturas 
    ) as criaturas 
    ON capturados.id_criatura = criaturas.num 
    GROUP BY criaturas.atributo 
    HAVING criaturas.atributo IS NOT NULL ;
""" 
# Requer nome_aventureiro e raridade = {"nome_aventureiro":str, "raridade": int}
select_capturados_raridade = lambda canal, idioma : f"""
    Select count(*) as QTDE_Capturados, 
    Count(CASE WHEN Especial = 1 THEN 1 END) As QTDE_Especial 
    FROM (
    SELECT capturados.Aventureiro_index, capturados.ID_Criatura, 
    capturados.especial, atributos.Nome_{idioma} as atr 
    FROM capturados_{canal} AS capturados 
    INNER JOIN atributos 
    ON atributos.id = capturados.golpe 
    WHERE aventureiro_index = ( 
    SELECT aventureiro_index 
    FROM aventureiros_{canal} 
    WHERE nome = :nome_aventureiro
    ) 
    ) as capturados 
    INNER JOIN ( 
    SELECT criaturas.num, criaturas.nome
    FROM criaturas
    WHERE custo = :raridade
    ) as criaturas 
    ON capturados.id_criatura = criaturas.num ; 
"""
# Requer nome_aventureiro = {"nome_aventureiro":str}
select_capturados_especial = lambda canal, idioma : f"""
    Select count(*) as QTDE_Capturados, 
    Count(CASE WHEN Especial = 1 THEN 1 END) As QTDE_Especial 
    FROM (
    SELECT capturados.Aventureiro_index, capturados.ID_Criatura, capturados.especial, 
    atributos.Nome_{idioma} as atr 
    FROM capturados_{canal} AS capturados 
    INNER JOIN atributos 
    ON atributos.id = capturados.golpe 
    WHERE aventureiro_index = ( 
    SELECT aventureiro_index 
    FROM aventureiros_{canal} 
    WHERE nome = :nome_aventureiro
    ) 
    AND capturados.especial = "1" 
    ) as capturados 
    INNER JOIN ( 
    SELECT criaturas.num, criaturas.nome 
    FROM criaturas 
    ) as criaturas 
    ON capturados.id_criatura = criaturas.num ;
"""