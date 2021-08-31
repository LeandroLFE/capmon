drop_table_aventureiros_canal = lambda dados = {} : f"""
    DROP TABLE IF EXISTS Aventureiros_{dados["canal_id"]};
"""

drop_table_capturados_canal = lambda dados = {} : f"""
    DROP TABLE IF EXISTS Capturados_{dados["canal_id"]};
"""

drop_table_buddies_canal = lambda dados = {} : f"""
    DROP TABLE IF EXISTS Buddies_{dados["canal_id"]};
"""

drop_capboard_dados_canal = lambda dados = {} : f"""
    DROP TABLE IF EXISTS Capboard_dados_{dados["canal_id"]};
"""

drop_itens_obtidos_canal = lambda dados = {} : f"""
    DROP TABLE IF EXISTS Itens_obtidos_{dados["canal_id"]};
"""