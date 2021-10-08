
def cap_command_messages_normal_horde (dados): 
    _item = "" if dados["item_usado"] == "" else f"used the {dados['item_usado']} item and "    
    if not dados["capturou"]:
        return f"""{dados["aventureiro"]} {_item}tried to catch the {dados["criatura"]["tipo"]} {dados["criatura"]["nome"]}, but it failed! Capcoins used: {dados["criatura"]["custo"]} """

    _pronta_evoluir = "" if  dados["capturaram"]["cp"] < dados["criatura"]["cp_limite"] else "The creature is ready to evolute, you can purchase the capevol or capevol+ item in the capshop"  
    _especial = "" if dados["capturaram"]["especial"] else " SPECIAL!!"

    return f"""{dados["aventureiro"]} has caught the {dados["criatura"]["tipo"]} {dados["criatura"]["nome"]}{_especial} Capcoins used: {dados["criatura"]["custo"]} {_pronta_evoluir}"""


error_horde_inactive = lambda dados : f'{dados["aventureiro"]}, now it´s not happening any horde!'