script_create_table_tipo_hordas = lambda dados = {} : """
    DROP TABLE IF EXISTS Tipo_hordas;

    CREATE TABLE Tipo_hordas (
        id INTEGER NOT NULL PRIMARY KEY,
        nome text NOT NULL,
        prioridade int NOT NULL DEFAULT 1
    );
"""

script_insert_table_tipo_hordas = lambda dados = {} : """INSERT INTO Tipo_hordas (id, nome, prioridade) VALUES (?, ?, ?);"""
dados_padrao_tabela_tipo_hordas = lambda dados = {} : [
    (1,"normal_aleatoria", 0),
    (2, "elemental", 1),
    (3, "capraid", 2),
    (4, "normal_especifica", 3)
]