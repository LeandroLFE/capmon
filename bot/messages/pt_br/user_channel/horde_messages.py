new_normal_horde_message = lambda horda = {} : f"""╔{"─"*(15-horda["criatura"]["custo"])}{"☆"*horda["criatura"]["custo"]}{"─"*(16-horda["criatura"]["custo"])}╗ Uma horda de {horda["criatura"]["nome_tipo"]} {horda["criatura"]["nome"]} apareceu! Digite !cap <numero_tentativas> para tentar capturar. Duração da horda: {horda["duracao"]}seg. Custo: {horda["criatura"]["custo"]}"""

def new_elemental_horde_message(horda = {}):
    _criaturas_nome_texto = ", ".join([c['nome'] for c in horda["criaturas"]])
    return f"""╔{"─"*(15-horda["custo"])}{"★"*horda["custo"]}{"─"*(16-horda["custo"])}╗ Uma horda elemental de criaturas do atributo {horda["atributo"]} e Custo {horda["custo"]} apareceu! Digite !cap <numero_tentativas> <nome_criatura> para tentar capturar. Opções: {_criaturas_nome_texto} Duração da horda: {horda["duracao"]}seg."""

new_capraid_message = lambda horda = {} : f"""╔{"─"*10}✦✧✦✧✦{"─"*10}╗ Lendário {horda["criatura"]["nome_tipo"]} {horda["criatura"]["nome"]} surgiu esperando por desafiantes! Digite !capraid para participar com seu capbuddy. Duração: {horda["duracao"]}seg."""

warning_finishing_normal_horde_message = lambda horda = {} : f"""╠{"─"*(15-horda["criatura"]["custo"])}{"☆"*horda["criatura"]["custo"]}{"─"*(16-horda["criatura"]["custo"])}╣ Uma horda de {horda["criatura"]["nome_tipo"]} {horda["criatura"]["nome"]} falta {horda["aviso"]}seg para finalizar. Digite !cap <numero_tentativas> para tentar capturar. ╠{"─"*(15-horda["criatura"]["custo"])}{"☆"*horda["criatura"]["custo"]}{"─"*(16-horda["criatura"]["custo"])}╣ """

def warning_finishing_elemental_horde_message (horda = {}): 
    _criaturas_nome_texto = ", ".join([c['nome'] for c in horda["criaturas"]])
    return f"""╠{"─"*(15-horda["custo"])}{"★"*horda["custo"]}{"─"*(16-horda["custo"])}╣ Uma horda elemental de criaturas do atributo {horda["atributo"]} e custo {horda["custo"]} está para finalizar em {horda["aviso"]}seg. Digite !cap <numero_tentativas> <nome_criatura> para tentar capturar. Opções: {_criaturas_nome_texto} ╠{"─"*(15-horda["custo"])}{"★"*horda["custo"]}{"─"*(16-horda["custo"])}╣ """

warning_finishing_capraid_message = lambda horda = {} : f"""╠{"─"*11}✦✧✦✧✦{"─"*11}╣ Uma capraid de {horda["criatura"]["nome_tipo"]} {horda["criatura"]["nome"]} falta {horda["aviso"]}seg para finalizar. Digite !capraid para participar com seu capbuddy. ╠{"─"*10}✦✧✦✧✦{"─"*10}╣ """

end_normal_horde_message = lambda horda = {} : f"""A horda foi embora. Próxima horda em {horda["tempo_espera"]} seg. ╚{"─"*(15-horda["criatura"]["custo"])}{"☆"*horda["criatura"]["custo"]}{"─"*(16-horda["criatura"]["custo"])}╝ """

end_normal_horde_message_offline_channel = lambda horda = {} : f"""A horda foi embora. Próxima horda quando o canal estiver online. ╚{"─"*(15-horda["criatura"]["custo"])}{"☆"*horda["criatura"]["custo"]}{"─"*(16-horda["criatura"]["custo"])}╝"""

end_elemental_horde_message = lambda horda = {} : f"""A horda Elemental acabou. Próxima horda em {horda["tempo_espera"]} seg. ╚{"─"*(15-horda["custo"])}{"★"*horda["custo"]}{"─"*(16-horda["custo"])}╝"""

end_elemental_horde_message_offline_channel = lambda horda = {} : f"""A horda Elemental acabou. Próxima horda quando o canal estiver online. ╚{"─"*(15-horda["custo"])}{"★"*horda["custo"]}{"─"*(16-horda["custo"])}╝ """

end_capraid_victory_message = lambda horda = {} : f"""A criatura lendaria se cansou de brincar e foi embora, mas chamou seus amigos para uma horda a seguir. ╚{"─"*10}✦✧✦✧✦{"─"*10}╝"""

end_capraid_victory_message_offline_channel = lambda horda = {} : f"""A criatura lendaria se cansou de brincar e foi embora, mas chamou seus amigos para uma horda quando o canal estiver online. ╚{"─"*10}✦✧✦✧✦{"─"*10}╝"""

end_capraid_defeat_message = lambda horda = {} : f"""A criatura lendaria se cansou de brincar e foi embora. Próxima horda em {horda["tempo_espera"]} seg. ╚{"─"*10}✦✧✦✧✦{"─"*10}╝ """

end_capraid_defeat_message_offline_channel = lambda horda = {} : f"""A criatura lendaria se cansou de brincar e foi embora. Próxima horda quando o canal estiver online. ╚{"─"*10}✦✧✦✧✦{"─"*10}╝ """