def tipo_horda(nome_horda):
    if nome_horda == "elemental":
        return "horda elemental"
    else:
        return "horda"


def cap_command_skip_message(
    dados): return f"""{dados["dados_aventureiro"]["nome"]} resolveu só assistir esta {tipo_horda(dados["nome_horda"])} sem gastar capcoins """


def cap_command_capture_messages(dados):
    _item = "" if dados["dados_horda"]["dados_aventureiro"][
        "item"] == "" else f"""usou o item {dados["dados_horda"]["dados_aventureiro"]['item']} e """
    if not dados["dados_horda"]["dados_aventureiro"]["capturou"]:
        return f"""{dados["dados_horda"]["dados_aventureiro"]["nome"]} {_item}tentou capturar a criatura {dados["dados_horda"]["criatura"]["nome_tipo"]} {dados["dados_horda"]["criatura"]["nome"]}, mas fugiu! Capcoins utilizados: {dados["dados_horda"]["criatura"]["custo"] * dados["dados_horda"]["dados_aventureiro"]["tentativas"]} """

    _criatura_ja_capturada = dados["dados_horda"]["criatura_ja_capturada"]
    _especial = "" if not _criatura_ja_capturada["especial"] else " ESPECIAL!!"
    _pronta_evoluir = "" if _criatura_ja_capturada["cp"] + dados["dados_horda"]["capturado"]["cp"] < dados["dados_horda"][
        "criatura"]["cp_limite"] else "A criatura está pronta pra evoluir, você pode obter o item capevol ou capevol+ no capshop"

    return f"""{dados["dados_horda"]["dados_aventureiro"]["nome"]} conseguiu capturar a criatura {dados["dados_horda"]["criatura"]["nome_tipo"]} {dados["dados_horda"]["criatura"]["nome"]}{_especial} Capcoins utilizados: {dados["dados_horda"]["criatura"]["custo"] * dados["dados_horda"]["dados_aventureiro"]["tentativas"]} {_pronta_evoluir}"""


def error_horde_inactive(
    dados): return f'{dados["aventureiro"]}, não há {tipo_horda(dados["nome_horda"])} ativa no momento!'


def error_adventure_already_participated(dados):
    has_captured = ", mas não conseguiu capturar a criatura" if not dados[
        "dados_aventureiro"]["capturou"] else " e conseguiu capturar a criatura"

    return f"""{dados["dados_aventureiro"]["nome"]} você já fez sua tentativa nessa {tipo_horda(dados["nome_horda"])}{has_captured}"""


def error_invalid_attempties(dados):
    opcoes = "" if dados[
        "nome_horda"] != "elemental" else f"""Opções: {','.join([c["nome"] for c in dados["criaturas"]])}"""
    creature = "" if dados["nome_horda"] != "elemental" else "<criatura> "
    return f"""{dados["aventureiro"]} , Favor enviar a quantidade de tentativas que deseja usar para capturar, !cap <numero> {creature}, Custo: {dados["custo"]} {opcoes}"""


def error_invalid_creature(
    dados): return f"""{dados["aventureiro"]}, criatura inválida, Opções: {', '.join(dados["opcoes"])}"""


def error_overload_attempties(
    dados): return f"""{dados["aventureiro"]}, o custo total excede a quantidade de capcoins que você possui. Custo da tentativa: {dados["custo"]} Capcoins atuais: {dados["capcoins"]}. Dica: Digite !cap 0 para pular esta horda e se manter na lista de adição de capcoins."""
