new_normal_horde_message = lambda horda = {} : f"""╔{"─"*(15-horda["criatura"]["custo"])}{"☆"*horda["criatura"]["custo"]}{"─"*(16-horda["criatura"]["custo"])}╗ A horde of {horda["criatura"]["nome_tipo"]} {horda["criatura"]["nome"]} has appeared! Tap !cap <attempties> to try to catch. Horde duration: {horda["duracao"]}sec. Cost: {horda["criatura"]["custo"]}"""

def new_elemental_horde_message(horda = {}):
    _criaturas_nome_texto = ", ".join([c['nome'] for c in horda["criaturas"]])
    return f"""╔{"─"*(15-horda["custo"])}{"★"*horda["custo"]}{"─"*(16-horda["custo"])}╗ The Elemental horde of creatures of the of the {horda["atributo"]} attribute and Cost {horda["custo"]} has appeared! Tap !cap <attempties> <creature> to try to catch. Options: {_criaturas_nome_texto} Horde duration: {horda["duracao"]}sec."""

new_capraid_message = lambda horda = {} : f"""╔{"─"*10}✦✧✦✧✦{"─"*10}╗ {horda["criatura"]["nome_tipo"]} {horda["criatura"]["nome"]} has appeared waiting for a challenge! Tap !capraid to participate with your capbuddy. Duration: {horda["duracao"]}sec."""

warning_finishing_normal_horde_message = lambda horda = {} : f"""╠{"─"*(15-horda["criatura"]["custo"])}{"☆"*horda["criatura"]["custo"]}{"─"*(16-horda["criatura"]["custo"])}╣ The horde of {horda["criatura"]["nome_tipo"]} {horda["criatura"]["nome"]} is lefting in {horda["aviso"]}sec. Tap !cap <attempties> to try to capture. ╠{"─"*(15-horda["criatura"]["custo"])}{"☆"*horda["criatura"]["custo"]}{"─"*(16-horda["criatura"]["custo"])}╣"""

def warning_finishing_elemental_horde_message (horda = {}): 
    _criaturas_nome_texto = ", ".join([c['nome'] for c in horda["criaturas"]])
    return f"""╠{"─"*(15-horda["custo"])}{"★"*horda["custo"]}{"─"*(16-horda["custo"])}╣ The Elemental horde of creatures of the attribute {horda["atributo"]} and cost {horda["custo"]} is lefting in {horda["aviso"]}sec. Tap !cap <attempties> <creature_name> to try to capture. Options: {_criaturas_nome_texto} ╠{"─"*(15-horda["custo"])}{"★"*horda["custo"]}{"─"*(16-horda["custo"])}╣ """

warning_finishing_capraid_message = lambda horda = {} : f"""╠{"─"*11}✦✧✦✧✦{"─"*11}╣ The horde of {horda["criatura"]["nome_tipo"]} {horda["criatura"]["nome"]} is lefting in {horda["aviso"]}sec. Tap !cap <attempties> to try to capture. ╠{"─"*10}✦✧✦✧✦{"─"*10}╣ """

end_normal_horde_message = lambda horda = {} : f"""The horde has gone. Next horde in {horda["tempo_espera"]} sec. ╚{"─"*(15-horda["criatura"]["custo"])}{"☆"*horda["criatura"]["custo"]}{"─"*(16-horda["criatura"]["custo"])}╝"""

end_normal_horde_message_offline_channel = lambda horda = {} : f"""The horde has gone. Next horde when the stream goes online. ╚{"─"*(15-horda["criatura"]["custo"])}{"☆"*horda["criatura"]["custo"]}{"─"*(16-horda["criatura"]["custo"])}╝"""

end_elemental_horde_message = lambda horda = {} : f"""The Elemental horde has gone. Next horde in {horda["tempo_espera"]} sec. ╚{"─"*(15-horda["custo"])}{"★"*horda["custo"]}{"─"*(16-horda["custo"])}╝"""

end_elemental_horde_message_offline_channel = lambda horda = {} : f"""The Elemental horde has gone. Next horde when the stream goes online. ╚{"─"*(15-horda["custo"])}{"★"*horda["custo"]}{"─"*(16-horda["custo"])}╝"""

end_capraid_victory_message = lambda horda = {} : f"""The legendary creature is tired of playing and went out, but it called its friends to a horde soon. ╚{"─"*10}✦✧✦✧✦{"─"*10}╝"""

end_capraid_victory_message_offline_channel = lambda horda = {} : f"""The legendary creature is tired of playing and went out, but it called its friends to a horde when the stream goes online. ╚{"─"*10}✦✧✦✧✦{"─"*10}╝"""

end_capraid_defeat_message = lambda horda = {} : f"""The legendary creature is tired of playing and went out. Next horde in {horda["tempo_espera"]} sec. ╚{"─"*10}✦✧✦✧✦{"─"*10}╝ """

end_capraid_defeat_message_offline_channel = lambda horda = {} : f"""The legendary creature is tired of playing and went out. Next horde when the stream goes online. ╚{"─"*10}✦✧✦✧✦{"─"*10}╝ """