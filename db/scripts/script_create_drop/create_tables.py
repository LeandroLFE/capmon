from db.default_data.default_create_table_with_underline_structure import default_create_table_structure_capturados, default_create_table_structure_aventureiros, default_create_table_structure_buddies, default_create_table_structure_capboard_dados, default_create_table_structure_items_obtidos

create_aventureiros_canal = lambda dados = {} : f"""
    CREATE TABLE IF NOT EXISTS Aventureiros_{dados["canal_id"]} (
        {default_create_table_structure_aventureiros()}
    );
"""

create_capturados_canal = lambda dados = {} : f"""
    CREATE TABLE IF NOT EXISTS Capturados_{dados["canal_id"]} (
        {default_create_table_structure_capturados()}
    );
"""

create_buddies_canal = lambda dados = {} : f"""
    CREATE TABLE IF NOT EXISTS Buddies_{dados["canal_id"]} (
        {default_create_table_structure_buddies()}
    );
"""

create_capboard_dados_canal = lambda dados = {} : f"""
    CREATE TABLE IF NOT EXISTS Capboard_dados_{dados["canal_id"]} (
        {default_create_table_structure_capboard_dados(dados)}
    );
"""

create_itens_obtidos_canal = lambda dados = {} : f"""
    CREATE TABLE IF NOT EXISTS Itens_obtidos_{dados["canal_id"]} (
        {default_create_table_structure_items_obtidos(dados)}
    );
"""