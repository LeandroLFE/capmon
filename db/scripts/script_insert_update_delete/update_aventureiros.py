'''
Requer: {
    "canal_id" : str,
    "parametros_aventureiro" : int,
    "aventureiro_id" : str,
}
'''

script_update_aventureiros_parametros = lambda dados = {}: f"""
    UPDATE Aventureiros_{dados["canal_id"]} 
    SET parametros_aventureiro = :parametros_aventureiro
    WHERE aventureiro_id = :aventureiro_id;
"""

'''
Requer: {
    "canal_id" : str,
    "aventureiros_id" : tuple,
}
'''

script_reset_cont_sequencia_outros_aventureiros = lambda dados= {}: f"""
    UPDATE Aventureiros_{dados["canal_id"]} 
    SET cont_sequencia_atual = 0
    WHERE aventureiro_id NOT IN ({dados["aventureiros_id"]});
"""
