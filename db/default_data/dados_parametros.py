script_create_table_parametros_hordas = lambda dados = {} : """
    DROP TABLE IF EXISTS Parametros_hordas;

    CREATE TABLE Parametros_hordas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        incremento_para_horda_elemental int NOT NULL,
        incremento_para_capraid int NOT NULL,
        tempo_horda_min int NOT NULL,
        tempo_horda_max int NOT NULL,
        tempo_entre_hordas_min int NOT NULL,
        tempo_entre_hordas_max int NOT NULL,
        aviso_horda_terminando_em_x_segundos int NOT NULL,
        faixa_pessoas_live_pequeno int NOT NULL,
        fator_cp_boss_capraid_live_pequeno_percent int NOT NULL ,
        faixa_pessoas_live_medio int NOT NULL,
        fator_cp_boss_capraid_live_medio_percent int NOT NULL,
        faixa_pessoas_live_grande int NOT NULL,
        fator_cp_boss_capraid_live_grande_percent int NOT NULL,
        fator_cp_boss_capraid_live_muito_grande_percent int NOT NULL
    );
"""

script_insert_table_parametros_hordas = lambda dados = {} : """
    INSERT INTO Parametros_hordas (incremento_para_horda_elemental, incremento_para_capraid, 
    tempo_horda_min, tempo_horda_max, 
    tempo_entre_hordas_min, tempo_entre_hordas_max, 
    aviso_horda_terminando_em_x_segundos,  
    faixa_pessoas_live_pequeno, fator_cp_boss_capraid_live_pequeno_percent, 
    faixa_pessoas_live_medio, fator_cp_boss_capraid_live_medio_percent,
    faixa_pessoas_live_grande, fator_cp_boss_capraid_live_grande_percent,
    fator_cp_boss_capraid_live_muito_grande_percent
    ) 
    VALUES (:incremento_para_horda_elemental, :incremento_para_capraid,
    :tempo_horda_min, :tempo_horda_max, 
    :tempo_entre_hordas_min, :tempo_entre_hordas_max, 
    :aviso_horda_terminando_em_x_segundos,  
    :faixa_pessoas_live_pequeno, :fator_cp_boss_capraid_live_pequeno_percent, 
    :faixa_pessoas_live_medio, :fator_cp_boss_capraid_live_medio_percent,
    :faixa_pessoas_live_grande, :fator_cp_boss_capraid_live_grande_percent,
    :fator_cp_boss_capraid_live_muito_grande_percent );
"""
dados_padrao_tabela_parametros_hordas = lambda dados = {} : {    
    "incremento_para_horda_elemental" : 20,
    "incremento_para_capraid" : 10,
    "tempo_horda_min" : 90,
    "tempo_horda_max" : 180,
    "tempo_entre_hordas_min": 180, 
    "tempo_entre_hordas_max" : 300,
    "aviso_horda_terminando_em_x_segundos" : 30,
    "faixa_pessoas_live_pequeno" : 50,
    "fator_cp_boss_capraid_live_pequeno_percent" : 20,
    "faixa_pessoas_live_medio" : 200,
    "fator_cp_boss_capraid_live_medio_percent" : 10,
    "faixa_pessoas_live_grande" : 1000,
    "fator_cp_boss_capraid_live_grande_percent" : 5,
    "fator_cp_boss_capraid_live_muito_grande_percent" : 1 ,  
}


script_create_table_parametros_criaturas = lambda dados = {} : """
    DROP TABLE IF EXISTS Parametros_criaturas;

    CREATE TABLE Parametros_criaturas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        cp_inicial int NOT NULL,
        chance_captura int NOT NULL,
        chance_especial int NOT NULL,
        num_tentativas_caso_zero_ou_negativo int NOT NULL
    );
"""
script_insert_table_parametros_criaturas = lambda dados = {} : """
    INSERT INTO Parametros_criaturas (cp_inicial, chance_captura, chance_especial, num_tentativas_caso_zero_ou_negativo)  
    VALUES (:cp_inicial, :chance_captura, :chance_especial, :num_tentativas_caso_zero_ou_negativo);
"""

dados_padrao_tabela_parametros_criaturas = lambda dados = {} : {
    "cp_inicial" : 250,
    "chance_captura" : 50,    
    "chance_especial" : 1,    
    "num_tentativas_caso_zero_ou_negativo" : 50,
}


script_create_table_parametros_aventureiros = lambda dados = {} : """
    DROP TABLE IF EXISTS Parametros_aventureiros;

    CREATE TABLE Parametros_aventureiros (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        capcoins_iniciais int NOT NULL,
        cont_hordas_para_add_capcoins int NOT NULL,
        cont_sequencia_para_add_capcoins_bonus int NOT NULL,
        add_capcoins_min int NOT NULL,
        add_capcoins_max int NOT NULL,
        add_capcoins_bonus_min int NOT NULL,
        add_capcoins_bonus_max int NOT NULL
    );
"""

script_insert_table_parametros_aventureiros = lambda dados = {} : """
    INSERT INTO Parametros_aventureiros (capcoins_iniciais, cont_hordas_para_add_capcoins, cont_sequencia_para_add_capcoins_bonus,
    add_capcoins_min, add_capcoins_max, add_capcoins_bonus_min, add_capcoins_bonus_max
    ) 
    VALUES (:capcoins_iniciais, :cont_hordas_para_add_capcoins, :cont_sequencia_para_add_capcoins_bonus,
    :add_capcoins_min, :add_capcoins_max, :add_capcoins_bonus_min, :add_capcoins_bonus_max );
"""

dados_padrao_tabela_parametros_aventureiros = lambda dados = {} : {
    "capcoins_iniciais" : 100,    
    "cont_hordas_para_add_capcoins" : 5,
    "cont_sequencia_para_add_capcoins_bonus" : 5,
    "add_capcoins_min" : 3,
    "add_capcoins_max" : 5,
    "add_capcoins_bonus_min" : 2,
    "add_capcoins_bonus_max" : 4   
}

script_create_table_parametros_buddies = lambda dados = {} : """
    DROP TABLE IF EXISTS Parametros_buddies;

    CREATE TABLE Parametros_buddies (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        qtde_hordas_para_add_cp int NOT NULL,
        add_cp_min int NOT NULL,
        add_cp_max int NOT NULL
    );
"""

script_insert_table_parametros_buddies = lambda dados = {} : """
    INSERT INTO Parametros_buddies (qtde_hordas_para_add_cp, add_cp_min, add_cp_max) 
    VALUES (:qtde_hordas_para_add_cp, :add_cp_min, :add_cp_max);
"""

dados_padrao_tabela_parametros_buddies = lambda dados = {} : {    
    "qtde_hordas_para_add_cp" : 5,
    "add_cp_min" : 4,
    "add_cp_max" : 6
}

script_create_table_parametros_capboard = lambda dados = {} : """
    DROP TABLE IF EXISTS Parametros_capboard;

    CREATE TABLE Parametros_capboard (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        add_vitoria int NOT NULL,
        add_derrota int NOT NULL,
        add_empate int NOT NULL,
        capcoins_primeiro int NOT NULL,
        capcoins_segundo int NOT NULL,
        capcoins_terceiro int NOT NULL
    );
"""
script_insert_table_parametros_capboard = lambda dados = {} : """
    INSERT INTO Parametros_capboard (add_vitoria, add_derrota, add_empate, capcoins_primeiro, capcoins_segundo, capcoins_terceiro) 
    VALUES (:add_vitoria, :add_derrota, :add_empate, :capcoins_primeiro, :capcoins_segundo, :capcoins_terceiro);
"""

dados_padrao_tabela_parametros_capboard = lambda dados = {} : {    
    "add_vitoria":3, 
    "add_derrota":1,
    "add_empate": 2,
    "capcoins_primeiro":15, 
    "capcoins_segundo":10, 
    "capcoins_terceiro":5
}