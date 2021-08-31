# Requer linha_evolutiva e forma = { "linha_evolutiva": int, "forma": int (1,2,3...)}
# Consultar tabela de criaturas caso de duvidas
select_evolucoes = lambda : """
    SELECT criaturas.Num, criaturas.Nome, criaturas.tipo, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.CP_Min, criaturas.CP_Max, criaturas.atributo1, criaturas.atributo2, criaturas.chance_especial, 
    criaturas.custo, criaturas.evolucao, criaturas.CP_limite, criaturas.Evolui
    FROM criaturas
    WHERE Linha_Evolutiva = :linha_evolutiva
    AND forma = :forma + 1
"""

select_evolucao_aleatoria = lambda : """
    SELECT criaturas.Num, criaturas.Nome, criaturas.tipo, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.CP_Min, criaturas.CP_Max, criaturas.atributo1, criaturas.atributo2, criaturas.chance_especial, 
    criaturas.custo, criaturas.evolucao, criaturas.CP_limite, criaturas.Evolui
    FROM criaturas
    WHERE Linha_Evolutiva = :linha_evolutiva
    AND forma = :forma + 1
    ORDER BY RAND() 
    LIMIT 1
"""
#  Seleciona criatura após devoluir para forma base
# Requer aventureiro_index e origem {"aventureiro_index": int, "origem": "int (Num da criatura em sua forma base)"}
select_evolucao_retorno_forma_base = lambda idioma, canal : f"""
    Select criaturas.num, criaturas.nome, capturados.CP, atributo, capturados.especial, 
    capturados.cont_capturados, criaturas.tipo, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.CP_Min, criaturas.CP_Max, criaturas.atributo1, criaturas.atributo2, 
    criaturas.chance_especial , criaturas.custo, criaturas.evolucao, criaturas.CP_limite, 
    criaturas.Evolui, capturados.aventureiro_index, capturados.Golpe, capturados.Origem 
    FROM (
    SELECT capturados.Aventureiro_index, capturados.ID_Criatura, capturados.CP, 
    atributos.Nome_{idioma} as atributo, atributos.tipo, capturados.especial, 
    capturados.cont_capturados, capturados.Golpe, capturados.Origem 
    FROM capturados_{canal} AS capturados 
    INNER JOIN atributos 
    ON capturados.Golpe = atributos.Id 
    WHERE aventureiro_index = :aventureiro_index 
    ) as capturados 
    INNER JOIN ( 
    SELECT criaturas.num, criaturas.tipo, criaturas.nome, criaturas.forma, criaturas.linha_evolutiva, 
    criaturas.CP_Min, criaturas.CP_Max, criaturas.atributo1, criaturas.atributo2, 
    criaturas.chance_especial , criaturas.custo, criaturas.evolucao, criaturas.CP_limite, 
    criaturas.Evolui 
    FROM criaturas 
    Where criaturas.num = :origem 
    ) as criaturas 
    ON capturados.id_criatura = criaturas.num 
    ORDER BY criaturas.custo DESC, capturados.CP DESC 
"""

