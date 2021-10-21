"""
Requer:
{
    "canal_id" : str,
    "aventureiro_id" : str,
    "nome_idioma" : str
}
"""

select_itens_obtidos_expirados_aventureiro_canal = lambda dados = "" : f"""
    Select IC.id, IC.id_item_capshop, IC.nome, IC.abreviacao, IC.custo_em_capcoins, Itens_obtidos.qtde, IC.descricao, 
    IC.valor_do_efeito, Comandos_uso_itens_capshop.comando, IC.item_capshop_plus, Itens_obtidos.data_expiracao, 
    Aventureiros.aventureiro_id, Aventureiros.nome as aventureiro_nome
    FROM Itens_obtidos_{dados["canal_id"]} as Itens_obtidos
    INNER JOIN Itens_capshop as IC
    ON IC.tipo_capshop = Itens_obtidos.tipo_item
    AND IC.id = Itens_obtidos.id_item
    INNER JOIN Comandos_uso_itens_capshop
    ON Comandos_uso_itens_capshop.id = IC.comando_uso_item
    INNER JOIN Aventureiros_{dados["canal_id"]} as Aventureiros 
    ON Aventureiros.aventureiro_id = Itens_obtidos.aventureiro_id
    WHERE data_expiracao <= date('Now', 'Localtime')
"""

"""
Requer:
{
    "canal_id" : str,
    "aventureiro_id" : str,
    "nome_idioma" : str
}
"""

select_itens_obtidos_capshop_aventureiro_canal = lambda dados = "" : f"""
    Select IC.id, IC.id_item_capshop, IC.nome, IC.abreviacao, IC.custo_em_capcoins, Itens_obtidos.qtde, IC.descricao, 
    IC.valor_do_efeito, Comandos_uso_itens_capshop.comando, IC.item_capshop_plus, Itens_obtidos.data_expiracao
    FROM Itens_obtidos_{dados["canal_id"]} as Itens_obtidos
    INNER JOIN Itens_capshop as IC
    ON IC.tipo_capshop = Itens_obtidos.tipo_item
    AND IC.id = Itens_obtidos.id_item
    INNER JOIN Comandos_uso_itens_capshop
    ON Comandos_uso_itens_capshop.id = IC.comando_uso_item
    WHERE Itens_obtidos.aventureiro_id = :aventureiro_id
    AND Itens_obtidos.qtde > 0;
"""

"""
Requer:
{
    "canal_id" : str,
    "aventureiro_id" : str,
    "nome_idioma" : str,
    "comando" : str,
    "abreviacao"  : str,
}
"""

script_consulta_uso_item_capshop = lambda dados = "" : f"""
    Select IC.id, IC.id_item_capshop, IC.nome, IC.abreviacao, IC.custo_em_capcoins, Itens_obtidos.qtde, IC.descricao, 
    IC.valor_do_efeito, Comandos_uso_itens_capshop.comando, IC.item_capshop_plus, Itens_obtidos.tipo_item, Itens_obtidos.data_expiracao
    FROM Itens_obtidos_{dados["canal_id"]} as Itens_obtidos
    INNER JOIN Itens_capshop as IC
    ON IC.tipo_capshop = Itens_obtidos.tipo_item
    AND IC.id = Itens_obtidos.id_item
    INNER JOIN Comandos_uso_itens_capshop
    ON Comandos_uso_itens_capshop.id = IC.comando_uso_item
    WHERE Itens_obtidos.aventureiro_id = :aventureiro_id
    AND Comandos_uso_itens_capshop.comando = :comando
    AND IC.abreviacao = :abreviacao
    AND Itens_obtidos.qtde > 0;
"""

"""
Requer:
{
    "canal_id" : str,
    "aventureiro_id" : str,
    "nome_idioma" : str
}
"""

select_itens_obtidos_capraid_aventureiro_canal = lambda dados = "" : f"""
    Select IC.id, IC.nome, IC.custo_em_porcentagem, Itens_obtidos.qtde, IC.descricao, 
    IC.valor_do_efeito, Itens_obtidos.data_expiracao
    FROM Itens_obtidos_{dados["canal_id"]} as Itens_obtidos
    INNER JOIN Itens_capraid as IC
    ON IC.tipo_capraid = Itens_obtidos.tipo_item
    AND IC.id = Itens_obtidos.id_item
    WHERE Itens_obtidos.aventureiro_id = :aventureiro_id;
"""