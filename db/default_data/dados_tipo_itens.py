script_create_table_tipo_itens = lambda dados = {} : """
    DROP TABLE IF EXISTS Tipo_itens;

    CREATE TABLE Tipo_itens (
        id INTEGER NOT NULL,
        canal_id text NOT NULL,
   
        FOREIGN KEY (canal_id)
            REFERENCES Canais(canal_id)
    );
"""