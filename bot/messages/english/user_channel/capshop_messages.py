def welcome(dados):
    plus = "+" if dados["plus"] else "" 
    mensagem = f"Bem vindo ao Capshop{plus} {'_'*22} "
    mensagem += f"Itens disponíveis: {'_'*30} "
    return mensagem

def capshop_items_msg(dados):
    mensagem = ""
    for i in dados["itens"]:
        mensagem += f"""#{i["id_item_capshop"]} -> {i["nome"]} capcoins : {i["custo_em_capcoins"]} : {i["descricao"]} """
    return mensagem

wait_for_user_to_buy = lambda dados = {} : f"Digite #capbuy #num para comprar, #capend para finalizar a sessão {'_' * 50} \r\n"

purchase_item = lambda dados = {} : f"""{dados["aventureiro_id"]} adquiriu o """

end_session = lambda dados = {} : "Sessao encerrada do Capshop, inicie uma nova com !capshop no chat da live"