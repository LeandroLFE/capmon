script_create_table_vantagens_subs = lambda dados = {} : """
    DROP TABLE IF EXISTS Vantagens_subs_perfis;

    CREATE TABLE Vantagens_subs_perfis (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        habilita_vantagens_subs int NOT NULL DEFAULT 1,
        aumento_chance_captura int NOT NULL,
        aumento_chance_especial int NOT NULL,
        acesso_exclusivo_capshop int NOT NULL,
        desconto_capshop_percent int NOT NULL
    );
"""

script_insert_table_vantagens_subs = lambda dados = {} : """
    INSERT INTO Vantagens_subs_perfis (habilita_vantagens_subs, aumento_chance_captura,
    aumento_chance_especial, acesso_exclusivo_capshop, desconto_capshop_percent) 
    VALUES (:habilita_vantagens_subs, :aumento_chance_captura,
    :aumento_chance_especial, :acesso_exclusivo_capshop, :desconto_capshop_percent);
"""

dados_padrao_tabela_vantagens_subs = lambda dados = {} : {    
    "habilita_vantagens_subs": 1, 
    "aumento_chance_captura": 10,
    "aumento_chance_especial": 4, 
    "acesso_exclusivo_capshop": 1,  
    "desconto_capshop_percent": 20
}