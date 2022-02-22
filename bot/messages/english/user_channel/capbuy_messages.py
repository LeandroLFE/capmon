invalid_parameter = lambda dados : """Parâmetro inválido. Dica: #capbuy #id_do_item dentre os existentes. Ex: #capbuy #1 """

without_capcoins = lambda dados : f"""Você não possui capcoins suficientes para comprar o item {dados["nome_item"]}, necessário {dados["custo_em_capcoins"]} capcoins. Possui: {dados["capcoins"]} capcoins."""

obtained_item = lambda dados : f"""{dados["aventureiro_nome"]} obteve o item {dados["nome_item"]} com sucesso. """

