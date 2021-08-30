default_create_table_structure_aventureiros = lambda dados = {} : """
    aventureiro_id text PRIMARY KEY,
    nome text NOT NULL,
    capcoins long NOT NULL DEFAULT 100,
    cont_hordas_atual int NOT NULL DEFAULT 0,
    cont_sequencia_atual int NOT NULL DEFAULT 0
"""

default_create_table_structure_items_obtidos = lambda dados = {} : f"""
    aventureiro_id text PRIMARY KEY,
    tipo_item int NOT NULL,
    id_item int NOT NULL DEFAULT 0,
    data_expiracao date NOT NULL default Now,

    FOREIGN KEY (aventureiro_id)
        REFERENCES Aventureiros_{dados["canal_id"]}(aventureiro_id)
"""

default_create_table_structure_capboard_dados = lambda dados = {} : f"""
    aventureiro_id text PRIMARY KEY,
    capbattlepoints int NOT NULL DEFAULT 0,

    FOREIGN KEY (aventureiro_id)
        REFERENCES Aventureiros_{dados["canal_id"]} (aventureiro_id)
"""

default_create_table_structure_buddies = lambda dados = {} : """
    aventureiro_id text PRIMARY KEY,
    id_criatura int NOT NULL,
    cont_Hordas_atual int NOT NULL DEFAULT 0
"""

default_create_table_structure_capturados = lambda dados = {} : """
    id_criatura INTEGER,
    aventureiro_id text,
    cp int NOT NULL,
    golpe text NOT NULL,
    especial int NOT NULL,
    origem int,

    FOREIGN KEY (id_criatura)
        REFERENCES criaturas (id),
    FOREIGN KEY (aventureiro_id)
        REFERENCES aventureiros (aventureiro_id),
    PRIMARY KEY(id_criatura, aventureiro_id) 
"""