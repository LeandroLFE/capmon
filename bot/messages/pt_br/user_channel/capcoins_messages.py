def msg_capcoins(dados):
    txt_itens_obtidos = ''
    if dados["itens_obtidos"] != []:
        txt_itens_obtidos = "; ".join([(i["nome"], i["qtde"], i["data_expiracao"]) for i in dados["items_obtidos"]])
        txt_itens_obtidos = f"""Itens obtidos: {txt_itens_obtidos}"""
    
    return f"""{dados["aventureiro_nome"]} possui {dados["capcoins"]} capcoins. {txt_itens_obtidos}"""

aventureiro_nao_encontrado = lambda dados = {} : """Aventureiro não encontrado na base de dados!"""
