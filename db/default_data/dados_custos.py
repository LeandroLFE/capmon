script_create_table_custos = lambda dados = {} : """
    DROP TABLE IF EXISTS Custos;

    CREATE TABLE Custos (
        id int NOT NULL PRIMARY KEY,
        nome text NOT NULL,
        idioma INTEGER NOT NULL,
        ref int NOT NULL,

        FOREIGN KEY (idioma)
            REFERENCES Idiomas(id)
    );
"""

script_insert_table_custos = lambda dados = {} : """INSERT INTO Custos (id, nome, idioma, ref) VALUES (?, ?, ?, ?);"""
dados_padrao_tabela_custos = lambda dados = {} : [
                                                (1,'common', 1, 1),
                                                (2,'uncommon', 1, 2),
                                                (3,'rare', 1, 3),
                                                (5,'legendary', 1, 5),
                                                (6,'comum', 2, 1),
                                                (7,'incomum', 2, 2),
                                                (8,'rara', 2, 3),
                                                (10,'lendaria', 2, 5)
                                                ]