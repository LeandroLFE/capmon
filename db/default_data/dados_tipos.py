script_create_table_tipos = lambda dados = {} : """
    DROP TABLE IF EXISTS Tipos;

    CREATE TABLE Tipos (
        id int NOT NULL PRIMARY KEY,
        nome text NOT NULL DEFAULT 'pokemon'
    );
"""

script_insert_table_tipos = lambda dados = {} : """INSERT INTO Tipos (id, nome) VALUES (?, ?);"""
dados_padrao_tabela_tipos = lambda dados = {} : [(1,'pokemon')]