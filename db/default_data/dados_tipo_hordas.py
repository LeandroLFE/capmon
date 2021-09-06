from db.default_data.default_create_table_with_underline_structure import default_create_table_structure_tipo_horda

script_create_table_tipo_hordas = lambda dados = {} : f"""
    DROP TABLE IF EXISTS Tipo_hordas;

    CREATE TABLE Tipo_hordas (
        {default_create_table_structure_tipo_horda()}
    );
"""

script_insert_table_tipo_hordas = lambda dados = {} : """INSERT INTO Tipo_hordas (id, nome, prioridade, percent_atual) VALUES (:tipo_horda_id, :nome_horda, :prioridade, :percent_atual);"""
dados_padrao_tabela_tipo_hordas = lambda dados = {"canal_id": ""} : [{
    "canal_id" : dados["canal_id"],
    "tipo_horda_id": 1, 
    "nome_horda": "normal_aleatoria", 
    "prioridade" : 0,
    "percent_atual" : 100
},{
    "canal_id" : dados["canal_id"],
    "tipo_horda_id": 2, 
    "nome_horda": "elemental", 
    "prioridade" : 1,
    "percent_atual" : 0
},{
    "canal_id" : dados["canal_id"],
    "tipo_horda_id": 3, 
    "nome_horda": "capraid", 
    "prioridade" : 2,
    "percent_atual" : 0
},{
    "canal_id" : dados["canal_id"],
    "tipo_horda_id": 4, 
    "nome_horda": "normal_especifica", 
    "prioridade" : 3,
    "percent_atual" : 0
}]