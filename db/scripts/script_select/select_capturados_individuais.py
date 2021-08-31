# Requer nome_aventureiro e tipo = {"nome_aventureiro":str, "tipo": int} 
select_capturados_tipo_individuais = lambda dados = {} : f"""
    Select criaturas.num, criaturas.nome, capturados.CP, atributo, capturados.especial, 
    capturados.cont_capturados, criaturas.tipo, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.CP_Min, criaturas.CP_Max, criaturas.atributo1, criaturas.atributo2, 
    criaturas.chance_especial , criaturas.custo, criaturas.evolucao, criaturas.CP_limite, 
    criaturas.Evolui, capturados.aventureiro_index, capturados.Golpe, capturados.Origem 
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
    SELECT criaturas.num, criaturas.tipo, criaturas.nome, criaturas.forma, 
    criaturas.linha_evolutiva, criaturas.CP_Min, criaturas.CP_Max, 
    criaturas.atributo1, criaturas.atributo2, criaturas.chance_especial, 
    criaturas.custo, criaturas.evolucao, criaturas.CP_limite, criaturas.Evolui 
    FROM criaturas 
    Where tipo = :tipo
    ) as criaturas 
    ON capturados.id_criatura = criaturas.num 
    ORDER BY criaturas.custo DESC, capturados.CP DESC 
"""
# Requer atributo, nome_aventureiro e tipo = {"atributo": int, "nome_aventureiro": str, "tipo": int}
select_capturados_atributo_individuais = lambda dados : f"""
    Select criaturas.num, criaturas.nome, capturados.CP, atributo, capturados.especial, 
    capturados.cont_capturados, criaturas.tipo, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.CP_Min, criaturas.CP_Max, criaturas.atributo1, criaturas.atributo2, 
    criaturas.chance_especial , criaturas.custo, criaturas.evolucao, criaturas.CP_limite, 
    criaturas.Evolui, capturados.aventureiro_index, capturados.Golpe, capturados.Origem 
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
    SELECT criaturas.num, criaturas.nome, criaturas.tipo, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.CP_Min, criaturas.CP_Max, criaturas.atributo1, criaturas.atributo2, 
    criaturas.chance_especial , criaturas.custo, criaturas.evolucao, 
    criaturas.CP_limite, criaturas.Evolui 
    FROM criaturas 
    Where atributo1 = :atributo
    Or atributo2 = :atributo
    ) as criaturas 
    ON capturados.id_criatura = criaturas.num 
    ORDER BY criaturas.custo DESC, capturados.CP DESC 
"""
# Requer nome_aventureiro e raridade = {"nome_aventureiro":str, "raridade": int}
select_capturados_raridade_individuais = lambda dados = {} :f"""
    Select criaturas.num, criaturas.nome, capturados.CP, atributo, capturados.especial, 
    capturados.cont_capturados, criaturas.tipo, criaturas.forma, 
    criaturas.linha_evolutiva, criaturas.CP_Min, criaturas.CP_Max, 
    criaturas.atributo1, criaturas.atributo2, criaturas.chance_especial, 
    criaturas.custo, criaturas.evolucao, criaturas.CP_limite, criaturas.Evolui, 
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
    SELECT criaturas.num, criaturas.nome, criaturas.tipo, criaturas.forma, 
    criaturas.linha_evolutiva, criaturas.CP_Min, criaturas.CP_Max, 
    criaturas.atributo1, criaturas.atributo2, criaturas.chance_especial , criaturas.custo, 
    criaturas.evolucao, criaturas.CP_limite, criaturas.Evolui 
    FROM criaturas 
    Where custo = :raridade
    ) as criaturas 
    ON capturados.id_criatura = criaturas.num 
    ORDER BY criaturas.custo DESC, capturados.CP DESC
"""

# Requer nome_aventureiro = {"nome_aventureiro":str}
select_capturados_especial_individuais = lambda dados = {} : f"""
    Select criaturas.num, criaturas.nome, capturados.CP, atributo, capturados.especial, 
    capturados.cont_capturados, criaturas.tipo, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.CP_Min, criaturas.CP_Max, criaturas.atributo1, criaturas.atributo2, 
    criaturas.chance_especial , criaturas.custo, criaturas.evolucao, criaturas.CP_limite, 
    criaturas.Evolui, capturados.aventureiro_index, capturados.Golpe, capturados.Origem 
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
    SELECT criaturas.num, criaturas.nome, criaturas.tipo, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.CP_Min, criaturas.CP_Max, criaturas.atributo1, criaturas.atributo2, 
    criaturas.chance_especial , criaturas.custo, criaturas.evolucao, 
    criaturas.CP_limite, criaturas.Evolui 
    FROM criaturas 
    ) as criaturas 
    ON capturados.id_criatura = criaturas.num 
    ORDER BY criaturas.custo DESC, capturados.CP DESC 
"""

# Requer id_aventureiro e num_criatura = {"id_aventureiro":int, "num_criatura" : int}
select_capturados_aventureiros = lambda dados : f"""
    SELECT capturados.ID_criatura, capturados.Aventureiro_index, capturados.CP, 
    criaturas.Evolucao, criaturas.forma, criaturas.Linha_evolutiva, criaturas.Evolui, capturados.Origem, 
    criaturas.CP_Min, criaturas.CP_Max, criaturas.atributo1, criaturas.atributo2, criaturas.chance_especial, 
    criaturas.Nome, criaturas.tipo, criaturas.CP_limite, criaturas.custo 
    FROM capturados_{dados["nome_canal"]} as capturados 
    INNER JOIN criaturas 
    ON capturados.ID_criatura = criaturas.num 
    WHERE Aventureiro_index = :id_aventureiro
    AND Origem = :num_criatura
"""
# Requer id_aventureiro e nome_criatura = {"id_aventureiro":int, "nome_criatura" : str}
select_capturados_aventureiro_nome = lambda dados : f"""
    SELECT capturados.ID_criatura, capturados.Aventureiro_index, capturados.CP, 
    criaturas.Evolucao, criaturas.forma, criaturas.Linha_evolutiva, criaturas.Evolui, capturados.Origem, 
    criaturas.CP_Min, criaturas.CP_Max, criaturas.atributo1, criaturas.atributo2, criaturas.chance_especial, 
    criaturas.Nome, criaturas.tipo, criaturas.CP_limite, 
    atributos.Nome_{dados["idioma"]} as atributo, capturados.Especial, criaturas.custo 
    FROM criaturas 
    INNER JOIN ( 
    capturados_{dados["nome_canal"]} as capturados 
    INNER JOIN atributos 
    ON capturados.Golpe = atributos.Id 
    ) 
    ON criaturas.num = capturados.ID_criatura 
    WHERE Aventureiro_index = :id_aventureiro 
    AND criaturas.Nome = :nome_criatura
"""

