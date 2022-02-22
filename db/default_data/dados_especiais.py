script_create_table_especiais = lambda dados = {} : """
    DROP TABLE IF EXISTS Especiais;

    CREATE TABLE Especiais (
        id int NOT NULL PRIMARY KEY,
        nome text NOT NULL,
        idioma INTEGER NOT NULL,
        ref int NOT NULL,

        FOREIGN KEY (idioma)
            REFERENCES Idiomas(id)
    );
"""

script_insert_table_especiais = lambda dados = {} : """INSERT INTO Especiais (id, nome, idioma, ref) VALUES (?, ?, ?, ?);"""
dados_padrao_tabela_especiais = lambda dados = {} : [
                                                (1,'special', 1, 1),
                                                (2,'specials', 1, 1)
                                                (3,'especial', 2, 1),
                                                (4,'especiais', 2, 1),
                                                ]