script_create_table_msg = lambda dados = {} : """
    DROP TABLE IF EXISTS Mensagens;

    CREATE TABLE Mensagens (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        canal_id text NOT NULL,
        msg text,
        
        FOREIGN KEY (canal_id)
            REFERENCES Canais (canal_id)        
    );
"""