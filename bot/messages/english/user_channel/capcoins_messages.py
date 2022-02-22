def msg_capcoins(dados):
    txt_itens_obtidos = ''
    if dados["itens_obtidos"] != []:
        aux_lista = []
        for i in dados["itens_obtidos"]:
            aux_itens = " : ".join((str(i["nome"]), str(i["qtde"]), str(i["data_expiracao"])))
            aux_lista.append(aux_itens)

        txt_itens_obtidos = "; ".join(aux_lista)
        txt_itens_obtidos = f"""Itens obtidos: {txt_itens_obtidos}"""
    
    return f"""{dados["aventureiro_nome"]} possui {dados["capcoins"]} capcoins. {txt_itens_obtidos}"""

msg_add_capcoins = lambda dados = {} : f"""{dados["moderador"]} adicionou {dados["capcoins"]} capcoins a {dados["aventureiro_nome"]}"""

person_not_found = lambda dados = {} : """Aventureiro não encontrado na base de dados! Comando correto: !capcoins+ <usuario> <valor>"""

invalid_amount = lambda dados = {} : """Quantidade de capcoins inválido! Comando correto: !capcoins+ <usuario> <valor>"""

not_allowed = lambda dados = {} : f"""{dados["moderador"]}, você precisa ser moderador para executar este comando!"""

