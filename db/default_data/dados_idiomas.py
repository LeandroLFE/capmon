
script_create_table_idiomas = lambda dados = {} : """
    DROP TABLE IF EXISTS Idiomas;

    CREATE TABLE Idiomas (
        id int NOT NULL PRIMARY KEY,
        nome text NOT NULL DEFAULT 'english'
    );
"""

script_insert_table_idiomas = lambda dados = {} : """
    INSERT INTO Idiomas (id, nome) 
    VALUES (:id, :nome_idioma);
"""
dados_padrao_tabela_idiomas = lambda dados = {} : [{    
    "id" : 1,
    "nome_idioma" : 'english'
    }, {
    "id" : 2, 
    "nome_idioma" : 'pt_br'
    }
]
