task_nova_horda_sync = lambda dados = {"canal_id": ""} : f"""nova_horda_sync_{dados["canal_id"]}"""
task_nova_horda_async = lambda dados = {"canal__id": ""} : f"""nova_horda_async_{dados["canal_id"]}"""
task_nova_horda_lendaria_sync = lambda dados = {"canal_id": ""} : f"""nova_horda_lendaria_sync_{dados["canal_id"]}"""
task_nova_horda_lendaria_async = lambda dados = {"canal_id": ""} : f"""nova_horda_lendaria_async_{dados["canal_id"]}"""


task_fim_horda_x_seg_antes_sync = lambda dados = {"canal_id": ""} : f"""fim_horda_x_seg_antes_sync_{dados["canal_id"]}"""
task_fim_horda_x_seg_antes_async = lambda dados = {"canal_id": ""} : f"""fim_horda_x_seg_antes_async_{dados["canal_id"]}"""
task_fim_horda_sync = lambda dados = {"canal_id": ""} : f"""fim_horda_sync_{dados["canal_id"]}"""
task_fim_horda_async = lambda dados = {"canal_id": ""} : f"""fim_horda_async_{dados["canal_id"]}"""
task_fim_horda_lendaria_sync = lambda dados = {"canal_id": ""} : f"""fim_horda_lendaria_sync_{dados["canal_id"]}"""
task_fim_horda_lendaria_async = lambda dados = {"canal_id": ""} : f"""fim_horda_lendaria_async_{dados["canal_id"]}"""

task_msg_canal = lambda dados = {"canal_id" : ""} : f"""msg_{dados["canal_id"]}"""

task_aguarda_expiracao_capmove = lambda dados = {"canal_id" : "" , "aventureiro_id" : ""} : f"""aguarda_expiracao_capmove_canal_id_{dados["canal_id"]}_aventureiro_id_{dados["aventureiro_id"]}"""
task_aguarda_expiracao_capbattle = lambda dados = {"canal_id" : "" , "aventureiro_id" : ""} : f"""aguarda_expiracao_capbattle_canal_id_{dados["canal_id"]}_aventureiro_id_{dados["aventureiro_id"]}"""
task_aguarda_cooldown_capbattle = lambda dados = {"canal_id" : "" , "aventureiro_id" : ""} : f"""aguarda_cooldown_capbattle_canal_id_{dados["canal_id"]}_aventureiro_id_{dados["aventureiro_id"]}"""
task_aguarda_expiracao_capshop = lambda dados = {"canal_id" : "" , "aventureiro_id" : ""} : f"""aguarda_expiracao_capshop_canal_id_{dados["canal_id"]}_aventureiro_id_{dados["aventureiro_id"]}"""
task_aguarda_expiracao_capmon = lambda dados = {"canal_id" : "" , "aventureiro_id" : ""} : f"""aguarda_expiracao_capmon_canal_id_{dados["canal_id"]}_aventureiro_id_{dados["aventureiro_id"]}"""