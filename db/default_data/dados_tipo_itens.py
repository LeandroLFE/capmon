script_create_table_tipo_itens = lambda dados = {} : """
    DROP TABLE IF EXISTS Tipo_itens;

    CREATE TABLE Tipo_itens (
        id INTEGER NOT NULL,
        canal_id text NOT NULL,
   
        FOREIGN KEY (canal_id)
            REFERENCES Canais(canal_id)
    );
"""

script_insert_table_tipo_itens = lambda dados = {} : """
    INSERT INTO Tipo_itens (id, canal_id)
    VALUES (:tipo_itens_id, :canal_id)
"""

dados_padrao_tabela_tipo_itens = lambda dados = {} : [{    
    "tipo_itens_id" : 1,
    "canal_id" : dados["canal_id"]
},{
    "tipo_itens_id" : 2,
    "canal_id" : dados["canal_id"]
}, 
]