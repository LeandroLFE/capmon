# Requer nome_aventureiro e tipo = {"nome_aventureiro":str, "tipo": int} 
select_capturados_tipo_individuais = lambda dados = {} : f"""
    Select Criaturas.num, Criaturas.nome, capturados.CP, atributo, capturados.especial, 
    capturados.cont_capturados, Criaturas.tipo, Criaturas.forma, Criaturas.linha_evolutiva, 
    Criaturas.CP_Min, Criaturas.CP_Max, Criaturas.atributo1, Criaturas.atributo2, 
    Criaturas.chance_especial , Criaturas.custo, Criaturas.evolucao, Criaturas.CP_limite, 
    Criaturas.Evolui, capturados.aventureiro_index, capturados.Golpe, capturados.Origem 
    FROM (
    SELECT capturados.Aventureiro_index, capturados.ID_Criatura, capturados.CP, 
    atributos.Nome_{dados["idioma"]} as atributo, atributos.tipo, capturados.especial, 
    capturados.cont_capturados, capturados.Golpe, capturados.Origem 
    FROM capturados_{dados["nome_canal"]} AS capturados 
    INNER JOIN atributos 
    ON capturados.Golpe = atributos.Id 
    WHERE aventureiro_index = ( 
    SELECT aventureiro_index 
    FROM aventureiros_{dados["nome_canal"]} 
    WHERE nome = :nome_aventureiro
    ) 
    ) as capturados 
    INNER JOIN ( 
    SELECT Criaturas.num, Criaturas.tipo, Criaturas.nome, Criaturas.forma, 
    Criaturas.linha_evolutiva, Criaturas.CP_Min, Criaturas.CP_Max, 
    Criaturas.atributo1, Criaturas.atributo2, Criaturas.chance_especial, 
    Criaturas.custo, Criaturas.evolucao, Criaturas.CP_limite, Criaturas.Evolui 
    FROM criaturas 
    Where tipo = :tipo
    ) as criaturas 
    ON capturados.id_criatura = Criaturas.num 
    ORDER BY Criaturas.custo DESC, capturados.CP DESC 
"""
# Requer atributo, nome_aventureiro e tipo = {"atributo": int, "nome_aventureiro": str, "tipo": int}
select_capturados_atributo_individuais = lambda dados : f"""
    Select Criaturas.num, Criaturas.nome, capturados.CP, atributo, capturados.especial, 
    capturados.cont_capturados, Criaturas.tipo, Criaturas.forma, Criaturas.linha_evolutiva, 
    Criaturas.CP_Min, Criaturas.CP_Max, Criaturas.atributo1, Criaturas.atributo2, 
    Criaturas.chance_especial , Criaturas.custo, Criaturas.evolucao, Criaturas.CP_limite, 
    Criaturas.Evolui, capturados.aventureiro_index, capturados.Golpe, capturados.Origem 
    FROM (
    SELECT capturados.Aventureiro_index, capturados.ID_Criatura, capturados.CP, 
    atributos.Nome_{dados["idioma"]} as atributo, capturados.especial, capturados.cont_capturados, 
    capturados.Golpe, capturados.Origem 
    FROM capturados_{dados["nome_canal"]} AS capturados 
    INNER JOIN atributos 
    ON capturados.Golpe = atributos.Id 
    WHERE aventureiro_index = ( 
    SELECT aventureiro_index 
    FROM aventureiros_{dados["nome_canal"]} 
    WHERE nome = :nome_aventureiro
    ) 
    ) as capturados 
    INNER JOIN ( 
    SELECT Criaturas.num, Criaturas.nome, Criaturas.tipo, Criaturas.forma, Criaturas.linha_evolutiva, 
    Criaturas.CP_Min, Criaturas.CP_Max, Criaturas.atributo1, Criaturas.atributo2, 
    Criaturas.chance_especial , Criaturas.custo, Criaturas.evolucao, 
    Criaturas.CP_limite, Criaturas.Evolui 
    FROM criaturas 
    Where atributo1 = :atributo
    Or atributo2 = :atributo
    ) as criaturas 
    ON capturados.id_criatura = Criaturas.id 
    ORDER BY Criaturas.custo DESC, capturados.CP DESC 
"""
# Requer nome_aventureiro e raridade = {"nome_aventureiro":str, "raridade": int}
select_capturados_raridade_individuais = lambda dados = {} :f"""
    Select Criaturas.num, Criaturas.nome, capturados.CP, atributo, capturados.especial, 
    capturados.cont_capturados, Criaturas.tipo, Criaturas.forma, 
    Criaturas.linha_evolutiva, Criaturas.CP_Min, Criaturas.CP_Max, 
    Criaturas.atributo1, Criaturas.atributo2, Criaturas.chance_especial, 
    Criaturas.custo, Criaturas.evolucao, Criaturas.CP_limite, Criaturas.Evolui, 
    capturados.aventureiro_index, capturados.Golpe, capturados.Origem 
    FROM (
    SELECT capturados.Aventureiro_index, capturados.ID_Criatura, capturados.CP, 
    atributos.Nome_{dados["idioma"]} as atributo, capturados.especial, 
    capturados.cont_capturados, capturados.Golpe, capturados.Origem 
    FROM capturados_{dados["nome_canal"]} AS capturados 
    INNER JOIN atributos 
    ON capturados.Golpe = atributos.ID 
    WHERE aventureiro_index = ( 
    SELECT aventureiro_index 
    FROM aventureiros_{dados["nome_canal"]} 
    WHERE nome = :nome_aventureiro
    ) 
    ) as capturados 
    INNER JOIN ( 
    SELECT Criaturas.num, Criaturas.nome, Criaturas.tipo, Criaturas.forma, 
    Criaturas.linha_evolutiva, Criaturas.CP_Min, Criaturas.CP_Max, 
    Criaturas.atributo1, Criaturas.atributo2, Criaturas.chance_especial , Criaturas.custo, 
    Criaturas.evolucao, Criaturas.CP_limite, Criaturas.Evolui 
    FROM criaturas 
    Where custo = :raridade
    ) as criaturas 
    ON capturados.id_criatura = Criaturas.id 
    ORDER BY Criaturas.custo DESC, capturados.CP DESC
"""

# Requer nome_aventureiro = {"nome_aventureiro":str}
select_capturados_especial_individuais = lambda dados = {} : f"""
    Select Criaturas.num, Criaturas.nome, capturados.CP, atributo, capturados.especial, 
    capturados.cont_capturados, Criaturas.tipo, Criaturas.forma, Criaturas.linha_evolutiva, 
    Criaturas.CP_Min, Criaturas.CP_Max, Criaturas.atributo1, Criaturas.atributo2, 
    Criaturas.chance_especial , Criaturas.custo, Criaturas.evolucao, Criaturas.CP_limite, 
    Criaturas.Evolui, capturados.aventureiro_index, capturados.Golpe, capturados.Origem 
    FROM (
    SELECT capturados.Aventureiro_index, capturados.ID_Criatura, capturados.CP, 
    atributos.Nome_{dados["idioma"]} as atributo, capturados.especial, capturados.cont_capturados, 
    capturados.Golpe, capturados.Origem 
    FROM capturados_{dados["nome_canal"]} AS capturados 
    INNER JOIN atributos 
    ON capturados.Golpe = atributos.Id 
    WHERE aventureiro_index = ( 
    SELECT aventureiro_index 
    FROM aventureiros_{dados["nome_canal"]} 
    WHERE nome = :nome_aventureiro 
    ) 
    AND capturados.especial = "1" 
    ) as capturados 
    INNER JOIN ( 
    SELECT Criaturas.num, Criaturas.nome, Criaturas.tipo, Criaturas.forma, Criaturas.linha_evolutiva, 
    Criaturas.CP_Min, Criaturas.CP_Max, Criaturas.atributo1, Criaturas.atributo2, 
    Criaturas.chance_especial , Criaturas.custo, Criaturas.evolucao, 
    Criaturas.CP_limite, Criaturas.Evolui 
    FROM criaturas 
    ) as criaturas 
    ON capturados.id_criatura = Criaturas.num 
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

