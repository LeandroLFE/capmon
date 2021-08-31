#   requer aventureiro_index = {"aventureiro_index": int (id do aventureiro)}
select_id_buddy_aventureiro = lambda dados = {} : f"""
    SELECT ID_criatura 
    FROM buddies_{dados["canal_id"]} 
    WHERE Aventureiro_index = :aventureiro_index "
"""

#   requer aventureiro_index = {"aventureiro_index": int (id do aventureiro)}
select_criatura_buddy = lambda dados = {} : f"""
    Select criaturas.num, criaturas.nome, capturados.CP, atributo, capturados.especial, 
    capturados.cont_capturados, criaturas.tipo, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.CP_Min, criaturas.CP_Max, criaturas.atributo1, criaturas.atributo2, 
    criaturas.chance_especial , criaturas.custo, criaturas.evolucao, criaturas.CP_limite, 
    criaturas.Evolui, capturados.aventureiro_index, capturados.Golpe, capturados.Origem 
    FROM (
    SELECT capturados.Aventureiro_index, capturados.ID_Criatura, capturados.CP, 
    atributos.Nome_{dados["idioma"]} as atributo, atributos.tipo, capturados.especial, 
    capturados.cont_capturados, capturados.Golpe, capturados.Origem 
    FROM capturados_{dados["canal_id"]} AS capturados 
    INNER JOIN atributos 
    ON capturados.Golpe = atributos.ID 
    WHERE aventureiro_index = :aventureiro_index
    ) as capturados 
    INNER JOIN ( 
    SELECT criaturas.num, criaturas.tipo, criaturas.nome, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.CP_Min, criaturas.CP_Max, criaturas.atributo1, criaturas.atributo2, 
    criaturas.chance_especial , criaturas.custo, criaturas.evolucao, 
    criaturas.CP_limite, criaturas.Evolui 
    FROM criaturas 
    INNER JOIN buddies_{dados["canal_id"]} 
    ON buddies_{dados["canal_id"]}.id_criatura = criaturas.num 
    WHERE buddies_{dados["canal_id"]}.aventureiro_index = :aventureiro_index 
    ) as criaturas 
    ON capturados.id_criatura = criaturas.num 
    AND capturados.tipo = criaturas.tipo 
    ORDER BY criaturas.custo DESC, capturados.CP DESC ;
"""