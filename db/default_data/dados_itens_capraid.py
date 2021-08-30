script_create_table_itens_capraid = lambda dados = {} : """
    DROP TABLE IF EXISTS Itens_capraid;

    CREATE TABLE Itens_capraid (
        id INTEGER NOT NULL,
        tipo_capraid int NOT NULL DEFAULT 2,
        nome text NOT NULL,
        custo_em_porcentagem int NOT NULL DEFAULT 0,
        descricao text,
        idioma int NOT NULL DEFAULT 1,

        FOREIGN KEY (tipo_capraid)
            REFERENCES Tipo_itens(id),
        FOREIGN KEY (idioma)
            REFERENCES Idiomas(id)
    );
"""