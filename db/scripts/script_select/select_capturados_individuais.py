"""
Requer :
{
  "canal_id": str,
  "aventureiro_id":str,
  "nome_idioma" : str, 
  "tipo": int
}
""" 
select_capturados_tipo_individuais = lambda dados : f"""
    Select Aventureiros.aventureiro_id, 
    Capturados.num, Capturados.nome, Capturados.cp, capturados.especial, 
    Capturados.tipo, Capturados.forma, Capturados.linha_evolutiva, 
    Capturados.cp_min, Capturados.cp_max, 
    Capturados.atributo1, Capturados.atributo2,
    Capturados.chance_especial , Capturados.custo, Capturados.nome_custo,
    Capturados.evolucao, Capturados.cp_limite, 
    Capturados.evolui, Capturados.golpe, Capturados.origem 
    FROM ( 
            SELECT aventureiro_id 
            FROM Aventureiros_{dados["canal_id"]} as Aventureiros 
            WHERE Aventureiros.aventureiro_id = :aventureiro_id
        ) as Aventureiros 
    INNER JOIN 
    ( 
        SELECT Capturados.aventureiro_id, Capturados.CP, Capturados.especial,
        Capturados.Golpe, Capturados.Origem, 
        Criaturas.num, Criaturas.nome, Criaturas.tipo, Criaturas.forma, Criaturas.linha_evolutiva, 
        Criaturas.CP_Min, Criaturas.CP_Max, 
        Criaturas.atributo1, Criaturas.atributo2, 
        Parametros_criaturas.chance_especial , Criaturas.custo, Custos.nome as nome_custo,
        Criaturas.evolucao, 
        Criaturas.CP_limite, Criaturas.Evolui 
        FROM Capturados_{dados["canal_id"]} as Capturados 
        INNER JOIN Criaturas 
        ON capturados.ID_Criatura = Criaturas.num
        INNER JOIN Parametros_criaturas
        ON Criaturas.parametro_criatura = Parametros_criaturas.id
        INNER JOIN Custos 
        ON Criaturas.custo = Custos.ref
        INNER JOIN Idiomas 
        ON Custos.idioma = Idiomas.id
        WHERE LOWER(Idiomas.nome) = LOWER(:nome_idioma)      
    ) as Capturados 
    ON aventureiros.aventureiro_id = Capturados.aventureiro_id 
    WHERE Capturados.tipo = :tipo 
    ORDER BY Capturados.custo DESC, capturados.CP DESC ;
"""

"""
Requer:
    { 
        "canal_id" : str,
        "aventureiro_id": str, 
        "nome_idioma" : str, 
        "atributo": int,
    }
"""
select_capturados_atributo_individuais = lambda dados : f"""
    Select Capturados.aventureiro_id, 
    Criaturas.num, Criaturas.nome, Capturados.cp, capturados.especial, 
    Criaturas.tipo, Criaturas.forma, Criaturas.linha_evolutiva, 
    Criaturas.cp_min, Criaturas.cp_max, 
    Criaturas.atributo1, Criaturas.atributo2,
    Criaturas.chance_especial , Criaturas.custo, Custos.nome as nome_custo,
    Criaturas.evolucao, Criaturas.cp_limite, 
    Criaturas.evolui, Capturados.golpe, Capturados.origem 
    FROM (
        SELECT capturados.aventureiro_id, capturados.ID_Criatura, capturados.CP, capturados.especial,
        capturados.Golpe, capturados.Origem 
        FROM Capturados_{dados["canal_id"]} AS capturados 
        INNER JOIN atributos 
        ON capturados.Golpe = atributos.Id 
        WHERE aventureiro_id = :aventureiro_id
    ) as capturados 
    INNER JOIN ( 
        SELECT Criaturas.num, Criaturas.nome, Criaturas.tipo, Criaturas.forma, Criaturas.linha_evolutiva, 
        Criaturas.CP_Min, Criaturas.CP_Max, 
        Criaturas.atributo1, Criaturas.atributo2, 
        Parametros_criaturas.chance_especial , Criaturas.custo, Criaturas.evolucao, 
        Criaturas.CP_limite, Criaturas.Evolui 
        FROM Criaturas 
        INNER JOIN Parametros_criaturas
        ON Criaturas.parametro_criatura = Parametros_criaturas.id 
        Where atributo1 = :atributo
        Or atributo2 = :atributo
    ) as Criaturas 
    ON Capturados.id_criatura = Criaturas.num
    INNER JOIN Custos 
    ON Criaturas.custo = Custos.ref
    INNER JOIN Idiomas 
    ON Custos.idioma = Idiomas.id
    WHERE LOWER(Idiomas.nome) = LOWER(:nome_idioma)
    ORDER BY Criaturas.custo DESC, Capturados.CP DESC ;
"""

"""
Requer:
    { 
        "canal_id" : str,
        "aventureiro_id": str, 
        "nome_idioma" : str, 
        "raridade": int,
    }
"""
select_capturados_raridade_individuais = lambda dados : f"""
    Select Capturados.aventureiro_id, 
    Criaturas.num, Criaturas.nome, Capturados.cp, capturados.especial, 
    Criaturas.tipo, Criaturas.forma, Criaturas.linha_evolutiva, 
    Criaturas.cp_min, Criaturas.cp_max, 
    Criaturas.atributo1, Criaturas.atributo2, 
    Criaturas.chance_especial , Criaturas.custo, Custos.nome as nome_custo, 
    Criaturas.evolucao, Criaturas.cp_limite, 
    Criaturas.evolui, Capturados.golpe, Capturados.origem 
    FROM (
        SELECT Capturados.aventureiro_id, Capturados.ID_Criatura, Capturados.CP, 
        Capturados.especial, Capturados.Golpe, Capturados.Origem 
        FROM Capturados_{dados["canal_id"]} AS capturados 
        INNER JOIN Atributos 
        ON capturados.Golpe = Atributos.ID 
        WHERE aventureiro_id = :aventureiro_id
    ) as Capturados 
    INNER JOIN ( 
        SELECT Criaturas.num, Criaturas.nome, Criaturas.tipo, Criaturas.forma, Criaturas.linha_evolutiva, 
        Criaturas.CP_Min, Criaturas.CP_Max, 
        Criaturas.atributo1, Criaturas.atributo2, 
        Parametros_criaturas.chance_especial , Criaturas.custo, Criaturas.evolucao, 
        Criaturas.CP_limite, Criaturas.Evolui 
        FROM Criaturas 
        INNER JOIN Parametros_criaturas
        ON Criaturas.parametro_criatura = Parametros_criaturas.id 
        Where custo = :raridade
    ) as Criaturas 
    ON capturados.id_criatura = Criaturas.num 
    INNER JOIN Custos 
    ON Criaturas.custo = Custos.ref
    INNER JOIN Idiomas 
    ON Custos.idioma = Idiomas.id
    WHERE LOWER(Idiomas.nome) = LOWER(:nome_idioma)
    ORDER BY Criaturas.custo DESC, capturados.CP DESC
"""

"""
Requer:
    { 
        "canal_id" : str,
        "aventureiro_id": str, 
        "nome_idioma" : str, 
    }
"""
select_capturados_especial_individuais = lambda dados : f"""
    Select Capturados.aventureiro_id, 
    Criaturas.num, Criaturas.nome, Capturados.cp, capturados.especial, 
    Criaturas.tipo, Criaturas.forma, Criaturas.linha_evolutiva, 
    Criaturas.cp_min, Criaturas.cp_max, 
    Criaturas.atributo1, Criaturas.atributo2, 
    Criaturas.chance_especial , Criaturas.custo, Custos.nome as nome_custo, Criaturas.evolucao, Criaturas.cp_limite, 
    Criaturas.evolui, Capturados.golpe, Capturados.origem 
    FROM (
        SELECT capturados.aventureiro_id, capturados.ID_Criatura, capturados.CP, 
        capturados.especial,
        capturados.Golpe, capturados.Origem 
        FROM Capturados_{dados["canal_id"]} AS capturados 
        INNER JOIN atributos 
        ON capturados.Golpe = atributos.Id 
        WHERE aventureiro_id = :aventureiro_id
        AND capturados.especial = "1" 
    ) as capturados 
    INNER JOIN ( 
        SELECT Criaturas.num, Criaturas.nome, Criaturas.tipo, Criaturas.forma, Criaturas.linha_evolutiva, 
        Criaturas.CP_Min, Criaturas.CP_Max, 
        Criaturas.atributo1, Criaturas.atributo2
        Parametros_criaturas.chance_especial , Criaturas.custo, Criaturas.evolucao, 
        Criaturas.CP_limite, Criaturas.Evolui 
        FROM criaturas 
        INNER JOIN Parametros_criaturas
        ON Criaturas.parametro_criatura = Parametros_criaturas.id 
    ) as criaturas 
    ON capturados.id_criatura = Criaturas.num 
    INNER JOIN Custos 
    ON Criaturas.custo = Custos.ref
    INNER JOIN Idiomas 
    ON Custos.idioma = Idiomas.id
    WHERE LOWER(Idiomas.nome) = LOWER(:nome_idioma)
    ORDER BY Criaturas.custo DESC, capturados.CP DESC  
"""


# Requer id_aventureiro e num_criatura = {"id_aventureiro":int, "num_criatura" : int}
select_capturados_aventureiros = lambda dados : f"""
    SELECT capturados.ID_criatura, capturados.Aventureiro_index, capturados.CP, 
    Criaturas.Evolucao, Criaturas.forma, Criaturas.Linha_evolutiva, Criaturas.Evolui, capturados.Origem, 
    Criaturas.CP_Min, Criaturas.CP_Max, Criaturas.atributo1, Criaturas.atributo2, Criaturas.chance_especial, 
    Criaturas.Nome, Criaturas.tipo, Criaturas.CP_limite, Criaturas.custo 
    FROM capturados_{dados["nome_canal"]} as capturados 
    INNER JOIN criaturas 
    ON capturados.ID_criatura = Criaturas.num 
    WHERE Aventureiro_index = :id_aventureiro
    AND Origem = :num_criatura
"""
# Requer id_aventureiro e nome_criatura = {"canal_id" : str, "aventureiro_id":str, "nome_criatura" : str}
select_capturados_aventureiro_nome = lambda dados : f"""
    SELECT Criaturas.id, Capturados.aventureiro_id, Capturados.cp, 
    Criaturas.evolucao, Criaturas.forma, Criaturas.linha_evolutiva, Criaturas.evolui, Capturados.origem, 
    Criaturas.cp_min, Criaturas.cp_max,  
    Atr1.nome AS "nome_atributo1",
    Atr2.nome AS "nome_atributo2", 
    Pc.chance_captura, 
    Pc.chance_especial,
    Criaturas.Nome, Criaturas.tipo, Criaturas.CP_limite, 
    Atrgolpe.nome as "golpe", Capturados.especial, Criaturas.custo 
    FROM Criaturas 
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
    LEFT JOIN 
    (
    SELECT Atributos.nome, Atributos.ref, Atributos.tipo, Idiomas.nome as nome_idioma_atr2
    FROM Atributos 
    INNER JOIN Idiomas 
    ON Atributos.idioma = Idiomas.id
    ) AS Atr2
    ON criaturas.atributo2 = Atr2.ref 
    AND criaturas.tipo = Atr2.tipo 
    INNER JOIN Capturados_{dados["canal_id"]} as Capturados 
    ON Criaturas.id = Capturados.origem
    INNER JOIN 
    (
        SELECT Atributos.nome, Atributos.ref, Atributos.tipo, Idiomas.nome as nome_idioma_golpe
        FROM Atributos
        INNER JOIN Idiomas 
        ON Atributos.idioma = Idiomas.id
    )   AS Atrgolpe
    ON Capturados.Golpe = Atrgolpe.ref 
    WHERE aventureiro_id = :aventureiro_id
    AND LOWER(Criaturas.nome) = LOWER(:nome_criatura)
"""

