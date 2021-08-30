script_create_table_atributos = lambda dados = {}: """
    DROP TABLE IF EXISTS Atributos;

    CREATE TABLE Atributos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        idioma INTEGER NOT NULL DEFAULT 1,
        nome text NOT NULL,
        tipo INTEGER NOT NULL DEFAULT 1,
        ref INTEGER NOT NULL,

        FOREIGN KEY (idioma)
            REFERENCES Idiomas (id),
        FOREIGN KEY (tipo)
            REFERENCES Tipos (id) 
    );
"""

script_insert_table_atributos = lambda dados = {} : """INSERT INTO Atributos (idioma, nome, tipo, ref) VALUES (?, ?, ?, ?);"""

dados_tabela_atributos_idioma= []

dados_tabela_atributos_idioma = {
    'english':[  
        (1, 'Bug', 1, 1),
        (1, 'Dragon', 1, 2),
        (1, 'Fairy', 1, 3),
        (1, 'Fire', 1, 4),
        (1, 'Ghost', 1, 5),
        (1, 'Ground', 1, 6),
        (1, 'Normal', 1, 7),
        (1, 'Psychic', 1, 8),
        (1, 'Steel', 1, 9),
        (1, 'Dark', 1, 10),
        (1, 'Electric', 1, 11),
        (1, 'Fighting', 1, 12),
        (1, 'Flying', 1, 13),
        (1, 'Grass', 1, 14),
        (1, 'Ice', 1, 15),
        (1, 'Poison', 1, 16),
        (1, 'Rock', 1, 17),
        (1, 'Water', 1, 18)
    ],

    'pt_br':[
        (2, 'Inseto', 1, 1),
        (2, 'Dragao', 1, 2),
        (2, 'Fada', 1, 3),
        (2, 'Fogo', 1, 4),
        (2, 'Fantasma', 1, 5),
        (2, 'Terra', 1, 6),
        (2, 'Normal', 1, 7),
        (2, 'Psiquico', 1, 8),
        (2, 'Metal', 1, 9),
        (2, 'Sombrio', 1, 10),
        (2, 'Eletrico', 1, 11),
        (2, 'Lutador', 1, 12),
        (2, 'Voador', 1, 13),
        (2, 'Planta', 1, 14),
        (2, 'Gelo', 1, 15),
        (2, 'Veneno', 1, 16),
        (2, 'Pedra', 1, 17),
        (2, 'Agua', 1, 18)
    ]}

lista_dados_tabela_atributos = []
for atributo_idioma in dados_tabela_atributos_idioma.values():
    lista_dados_tabela_atributos += atributo_idioma

dados_padrao_tabela_atributos = lambda dados = {} : lista_dados_tabela_atributos