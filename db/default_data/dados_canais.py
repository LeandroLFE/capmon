script_create_table_canais = lambda dados = {} : """
    DROP TABLE IF EXISTS Canais;

    CREATE TABLE Canais (
        canal_id text NOT NULL,
        nome_canal text NOT NULL,
        idioma int NOT NULL,
        ativo int NOT NULL,
        perfil_vantagens_subs int NOT NULL,
        parametros_capboard int NOT NULL DEFAULT 1,
        parametros_hordas int NOT NULL DEFAULT 1,
        parametros_aventureiros int NOT NULL DEFAULT 1,
        
        PRIMARY KEY (canal_id),
        FOREIGN KEY (idioma)
            REFERENCES Idiomas(id),
        FOREIGN KEY (parametros_aventureiros)
            REFERENCES Parametros_aventureiros(id),
        FOREIGN KEY (parametros_capboard)
            REFERENCES Parametros_capboard(parametros_capboard),
        FOREIGN KEY (parametros_hordas)
            REFERENCES Parametros_hordas(parametros_horda)
    );
"""