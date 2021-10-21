script_create_table_itens_capraid = lambda dados = {} : """
    DROP TABLE IF EXISTS Itens_capraid;

    CREATE TABLE Itens_capraid (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_capraid int NOT NULL DEFAULT 2,
        nome text NOT NULL,
        custo_em_porcentagem int NOT NULL DEFAULT 0,
        valor_do_efeito long NOT NULL,
        descricao text,
        idioma int NOT NULL DEFAULT 1,

        FOREIGN KEY (tipo_capraid)
            REFERENCES Tipo_itens(id),
        FOREIGN KEY (idioma)
            REFERENCES Idiomas(id)
    );
"""

script_insert_table_itens_capraid = lambda dados = {} : """
    INSERT INTO Itens_capraid (tipo_capraid, nome, custo_em_porcentagem, valor_do_efeito, descricao, idioma)
    VALUES (:tipo_capraid, :nome, :custo_em_porcentagem, :valor_do_efeito, :descricao, :idioma)
"""
_itens_capraid = [{
    "tipo_capraid":2, 
    "nome":"Capmove", 
    "custo_em_porcentagem":10, 
    "valor_do_efeito" : 2,
    "descricao": "Double CP temporarily, enable Z finished commands", 
    "idioma" : 1
},{
    "tipo_capraid":2, 
    "nome":"Capmove", 
    "custo_em_porcentagem":10,
    "valor_do_efeito" : 2, 
    "descricao": "Dobra CP temporariamente, habilita comandos terminados em Z", 
    "idioma" : 2
}]

dados_padrao_tabela_itens_capraid = lambda dados = {} : _itens_capraid