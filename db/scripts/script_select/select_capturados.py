"""
Requer :
{
  "canal_id": str,
  "aventureiro_id":str, 
  "tipo": int
}
""" 
select_capturados_tipo = lambda dados : f"""
    Select COUNT(*) as QTDE_Capturados,  
    Count(CASE WHEN Especial = 1 THEN 1 END) As QTDE_Especial, 
    capturados.tipo 
    FROM ( 
            SELECT nome, aventureiro_id 
            FROM aventureiros_{dados["canal_id"]} as aventureiros 
            WHERE aventureiros.aventureiro_id = :aventureiro_id
        ) as aventureiros 
        LEFT JOIN 
        ( 
            SELECT capturados.aventureiro_id, capturados.ID_Criatura, 
            criaturas.tipo, capturados.especial 
            FROM capturados_{dados["canal_id"]} as capturados 
            INNER JOIN criaturas 
            ON capturados.ID_Criatura = criaturas.num 
        ) as capturados 
        ON aventureiros.aventureiro_id = capturados.aventureiro_id 
    GROUP BY capturados.aventureiro_id, capturados.tipo 
    HAVING capturados.tipo = :tipo ;
"""

"""
Requer:
    { 
        "canal_id" : str,
        "aventureiro_id": str, 
        "atributo": int,
    }
"""
select_capturados_atributo = lambda dados : f"""
    Select count(*) as QTDE_Capturados, Count(CASE WHEN Especial = 1 THEN 1 END) As QTDE_Especial 
    FROM (
        SELECT Capturados.aventureiro_id, Capturados.id_criatura, Capturados.especial 
        FROM Capturados_{dados["canal_id"]} AS capturados 
        WHERE Capturados.aventureiro_id = :aventureiro_id
    ) as capturados 
    INNER JOIN ( 
        SELECT criaturas.num, criaturas.nome, (
            CASE WHEN atributo1 = :atributo
            THEN atributo1 
        ELSE (
            CASE WHEN atributo2 = :atributo
            THEN atributo2 
            ELSE NULL 
            END ) 
        END ) AS Atributo 
    FROM criaturas 
    ) as criaturas 
    ON capturados.id_criatura = criaturas.num 
    GROUP BY criaturas.atributo 
    HAVING criaturas.atributo IS NOT NULL ;
"""

"""
Requer:
    { 
        "canal_id" : str,
        "aventureiro_id": str, 
        "raridade": int,
    }
"""
select_capturados_raridade = lambda dados : f"""
    Select count(*) as QTDE_Capturados, 
    Count(CASE WHEN Especial = 1 THEN 1 END) As QTDE_Especial 
    FROM (
        SELECT capturados.aventureiro_id, capturados.ID_Criatura, 
        capturados.especial
        FROM capturados_{dados["canal_id"]} AS capturados 
        INNER JOIN atributos 
        ON atributos.id = capturados.golpe 
        WHERE aventureiro_id = :aventureiro_id
    ) as capturados 
    INNER JOIN ( 
        SELECT criaturas.num, criaturas.nome
        FROM criaturas
        WHERE custo = :raridade
    ) as criaturas 
    ON capturados.id_criatura = criaturas.num ; 
"""

"""
Requer:
    { 
        "canal_id" : str,
        "aventureiro_id": str
    }
"""

select_capturados_especial = lambda dados : f"""
    Select count(*) as QTDE_Capturados, 
    count(CASE WHEN Especial = 1 THEN 1 END) As QTDE_Especial 
    FROM (
        SELECT capturados.aventureiro_id, capturados.ID_Criatura, capturados.especial
        FROM capturados_{dados["canal_id"]} AS capturados 
        INNER JOIN atributos 
        ON atributos.id = capturados.golpe 
        WHERE aventureiro_id = :aventureiro_id
        AND capturados.especial = "1" 
    ) as capturados 
    INNER JOIN ( 
        SELECT criaturas.num, criaturas.nome 
        FROM criaturas 
    ) as criaturas 
    ON capturados.id_criatura = criaturas.num ;
"""