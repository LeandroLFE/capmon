msg_no_creatures = lambda dados : f"""{dados["aventureiro_nome"]} Você não possui criaturas com o filtro especificado!"""

msg_invalid_filter = lambda dados : f"""{dados["aventureiro_nome"]} Favor informar um filtro, !caplist <tipo> para listar outras opções, Tipos disponíveis: {dados["lista_tipos"]}"""

def msg_show_captured(dados):
    _type_or_attibute = "tipo" if dados["tipo_ou_atributo"] == "type" else "atributo"
    return f"""{dados["aventureiro_nome"]}, você possui {dados["qtde"]} criaturas do {_type_or_attibute} {dados["filtro"]}, sendo {dados["qtde_especial"]} especiais"""
