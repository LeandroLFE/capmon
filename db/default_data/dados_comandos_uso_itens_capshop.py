script_create_table_comandos_uso_itens_capshop = lambda dados = {} : """
    DROP TABLE IF EXISTS Comandos_uso_itens_capshop;

    CREATE TABLE Comandos_uso_itens_capshop (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        comando text NOT NULL
    );
"""

script_insert_table_comandos_uso_itens_capshop = lambda dados = {} : """
    INSERT INTO Comandos_uso_itens_capshop (id, comando)
    VALUES (:comandos_uso_itens_capshop_id, :comando)
"""

dados_padrao_tabela_comandos_uso_itens_capshop = lambda dados = {} : [{    
    "comandos_uso_itens_capshop_id" : 1,
    "comando" : "capuse"
},{
    "comandos_uso_itens_capshop_id" : 2,
    "comando" : "cap"
},{
    "comandos_uso_itens_capshop_id" : 3,
    "comando" : "capbattle"
}]