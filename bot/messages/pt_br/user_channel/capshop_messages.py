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

wait_for_user_to_buy = lambda dados = {} : f"Digite #comprar #num para comprar, #capend para finalizar a sessão {'_' * 50} \r\n"