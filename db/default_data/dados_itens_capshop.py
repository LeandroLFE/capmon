script_create_table_itens_capshop = lambda dados = {} : """
    DROP TABLE IF EXISTS Itens_capshop;

    CREATE TABLE Itens_capshop (
        id INTEGER NOT NULL,
        tipo_capshop int NOT NULL DEFAULT 1,
        id_item_capshop text NOT NULL,
        nome text NOT NULL,
        custo_em_capcoins int NOT NULL DEFAULT 0,
        descricao text,
        idioma int NOT NULL DEFAULT 1,
        item_capshop_plus int DEFAULT 0,

        FOREIGN KEY (tipo_capshop)
            REFERENCES Tipo_itens(id),
        FOREIGN KEY (idioma)
            REFERENCES Idiomas(id)
    );
"""