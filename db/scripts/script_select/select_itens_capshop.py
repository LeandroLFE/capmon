'''
Requer:
{
    "nome_idioma" : str,
}
'''

script_select_itens_capshop = lambda dados = {} : f"""
    SELECT IC.id, tipo_capshop, id_item_capshop, IC.nome, abreviacao, custo_em_capcoins, descricao, valor_do_efeito, Comandos_uso_itens_capshop.comando, Idiomas.nome as nome_idioma, item_capshop_plus
    FROM Itens_capshop as IC
    INNER JOIN Comandos_uso_itens_capshop
    ON Comandos_uso_itens_capshop.id = IC.comando_uso_item
    INNER JOIN Idiomas
    ON IC.idioma = Idiomas.id
    WHERE Idiomas.nome = :nome_idioma
    ORDER BY id_item_capshop
"""