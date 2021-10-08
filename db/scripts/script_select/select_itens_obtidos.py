select_itens_obtidos_aventureiro_canal = lambda dados = "" : f"""
    Select IC.id, IC.id_item_capshop, IC.nome, IC.abreviacao, IC.custo_em_capcoins, IC.descricao, 
    IC.valor_efeito, Comandos_uso_itens_capshop.comando, IC.item_capshop_plus, Itens_obtidos.data_expiracao
    FROM Comandos_uso_itens_capshop
    INNER JOIN Itens_capshop as IC
    ON Comandos_uso_itens_capshop.id = IC.comando_uso_item
    INNER JOIN Itens_obtidos_{dados["canal_id"]} as Itens_obtidos
    ON IC.id = Itens_obtidos.id_item
    AND IC.tipo_capshop = Itens_obtidos.tipo_item
    WHERE Itens_obtidos.aventureiro_id = :aventureiro_id
    AND IC.idioma = :nome_idioma
"""