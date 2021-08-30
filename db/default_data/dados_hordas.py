script_create_table_hordas = lambda dados = {} : """
    DROP TABLE IF EXISTS Hordas;

    CREATE TABLE Hordas (
        tipo_horda int NOT NULL,
        canal_id text NOT NULL,
        horda_ativa int NOT NULL DEFAULT 1,
        percent_atual int NOT NULL DEFAULT 0,

        FOREIGN KEY (tipo_horda)
            REFERENCES Tipo_hordas(id),
        FOREIGN KEY (canal_id)
            REFERENCES Canais(canal_id)
    );
"""