msg_no_creatures = lambda dados : f"""{dados["aventureiro_nome"]} Você não possui criaturas com o filtro especificado!"""

# msg_invalid_filter = lambda dados : f"""{dados["aventureiro_nome"]} Favor informar um filtro, !caplist <tipo> para listar outras opções, Tipos disponíveis: {dados["lista_tipos"]}"""

msg_invalid_filter = lambda dados : f"""{dados["aventureiro_nome"]} Favor informar um filtro válido, Tipos: {dados["lista_tipos"]} ; Atributos: {dados["lista_atributos"]} ; Raridades: {dados["lista_raridades"]} ; Outros: {dados["lista_especiais"]} """

def msg_show_captured(dados):
    if dados["tipo_exibido"] == "type":
        _type_to_show = "do tipo " 
    elif dados["tipo_exibido"] == "attribute": 
        _type_to_show = "do atributo "
    elif dados["tipo_exibido"] == "rarity": 
        _type_to_show = "da raridade "
    else:
        _type_to_show = "especiais"


    if dados["tipo_exibido"] != "other":
        saida = f"""{dados["aventureiro_nome"]}, você possui {dados["qtde"]} criaturas {_type_to_show}{dados["filtro"]}, sendo {dados["qtde_especial"]} especiais""" 
    else:
        saida = f"""{dados["aventureiro_nome"]}, você possui {dados["qtde"]} criaturas {_type_to_show}""" 
    
    return saida

msg_start_show_captured_whisper = lambda dados : f"""{dados["aventureiro_nome"]} Suas criaturas aparecerão abaixo:"""

def msg_show_captured_whisper(dados):
    saida = ""
    for raridade in dados["raridades"]:
        saida += f"{raridade.upper()}: "
        lista_criaturas_saida = []
        for criatura in dados["criaturas"][raridade]:
            especial = " ESPECIAL" if {criatura["especial"]} == 1 else "" 
            lista_criaturas_saida += [f"""{criatura["nome"]}{especial}"""] 
        saida += ", ".join(lista_criaturas_saida)
        saida += " ; "
    return saida

end_session = lambda dados = {} : "Sessao encerrada do Capmon, inicie uma nova com !capmon <filtro> no chat da live"