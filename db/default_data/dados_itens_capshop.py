script_create_table_itens_capshop = lambda dados = {} : """
    DROP TABLE IF EXISTS Itens_capshop;

    CREATE TABLE Itens_capshop (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_capshop int NOT NULL DEFAULT 1,
        id_item_capshop text NOT NULL,
        nome text NOT NULL,
        abreviacao text NOT NULL,
        custo_em_capcoins int NOT NULL DEFAULT 0,
        descricao text,
        valor_do_efeito int NOT NULL,
        comando_uso_item int NOT NULL,
        idioma int NOT NULL DEFAULT 1,
        item_capshop_plus int DEFAULT 0,

        FOREIGN KEY (tipo_capshop)
            REFERENCES Tipo_itens(id),
        FOREIGN KEY (comando_uso_item)
            REFERENCES Comandos_uso_itens_capshop(id),
        FOREIGN KEY (idioma)
            REFERENCES Idiomas(id)
    );
"""

script_insert_table_itens_capshop = lambda dados = {} : """
    INSERT INTO Itens_capshop (tipo_capshop, id_item_capshop, nome, abreviacao, custo_em_capcoins, descricao, valor_do_efeito, comando_uso_item, idioma, item_capshop_plus)
    VALUES (:tipo_capshop, :id_item_capshop, :nome, :abreviacao, :custo_em_capcoins, :descricao, :valor_do_efeito, :comando_uso_item, :idioma, :item_capshop_plus)
"""
_itens_capshop = [{
    "tipo_capshop": 1, 
    "id_item_capshop": '1', 
    "nome":"Capchance",
    "abreviacao":"chance", 
    "custo_em_capcoins":50, 
    "descricao": f"increase the capture chance {'_'*33} ", 
    "valor_do_efeito" : 5,
    "comando_uso_item" : 2,
    "idioma": 1, 
    "item_capshop_plus": 0
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '1', 
    "nome":"Capchance", 
    "abreviacao":"chance",
    "custo_em_capcoins":50, 
    "descricao": f"aumenta chances de captura {'_'*28} ",
    "valor_do_efeito" : 5, 
    "comando_uso_item" : 2,
    "idioma": 2, 
    "item_capshop_plus": 0
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '2', 
    "nome":"Capspecial", 
    "abreviacao":"special",
    "custo_em_capcoins":100, 
    "descricao": f"increase the Special chance {'_'*34} ", 
    "valor_do_efeito" : 5,
    "comando_uso_item" : 2, 
    "idioma": 1, 
    "item_capshop_plus": 0
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '2', 
    "nome":"Capspecial", 
    "abreviacao":"special",
    "custo_em_capcoins":100, 
    "descricao": f"aumenta chances de especial {'_'*28} ", 
    "valor_do_efeito" : 5, 
    "comando_uso_item" : 2,
    "idioma": 2, 
    "item_capshop_plus": 0
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '3', 
    "nome":"Capcandy", 
    "abreviacao":"capcandy",
    "custo_em_capcoins":50, 
    "descricao": f"increase a creature CP {'_' * 36}",
    "valor_do_efeito" : 0,  
    "comando_uso_item" : 1,
    "idioma": 1, 
    "item_capshop_plus": 0
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '3', 
    "nome":"Capcandy", 
    "abreviacao":"capcandy",
    "custo_em_capcoins":50, 
    "descricao": f"aumenta o CP de uma criatura {'_'*31} ",
    "valor_do_efeito" : 0,  
    "comando_uso_item" : 1,
    "idioma": 2, 
    "item_capshop_plus": 0
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '4', 
    "nome":"Capevol", 
    "abreviacao":"capevol",
    "custo_em_capcoins":50, 
    "descricao": f"Evolve an able creature to a random stage {'_'*20} ", 
    "valor_do_efeito" : 0, 
    "comando_uso_item" : 1,
    "idioma": 1, 
    "item_capshop_plus": 0
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '4', 
    "nome":"Capevol", 
    "abreviacao":"capevol",
    "custo_em_capcoins":50, 
    "descricao": f"Evolui uma criatura apta para um estágio aleatório {'_'*15} ", 
    "valor_do_efeito" : 0, 
    "comando_uso_item" : 1,
    "idioma": 2, 
    "item_capshop_plus": 0
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '5', 
    "nome":"Capswap", 
    "abreviacao":"swap",
    "custo_em_capcoins":10, 
    "descricao": f"Swap the atk from a creature that has 2 attributes {'_'*12} ", 
    "valor_do_efeito" : 0, 
    "comando_uso_item" : 3,
    "idioma": 1, 
    "item_capshop_plus": 0
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '5', 
    "nome":"Capswap", 
    "abreviacao":"swap",
    "custo_em_capcoins":10, 
    "descricao": f"Alterna o atributo do atk de uma criatura de 2 tipos {'_'*15} ",  
    "valor_do_efeito" : 0, 
    "comando_uso_item" : 3,
    "idioma": 2,
    "item_capshop_plus": 0
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '6', 
    "nome":"Capshield", 
    "abreviacao":"shield",
    "custo_em_capcoins":10, 
    "descricao": f"Prevents a creature to receive a super effective atk from a 2 attributes creature {'_'*30} ", 
    "valor_do_efeito" : 0, 
    "comando_uso_item" : 3,
    "idioma": 1, 
    "item_capshop_plus": 0
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '6', 
    "nome":"Capshield", 
    "abreviacao":"shield",
    "custo_em_capcoins":10, 
    "descricao": f"Impede uma criatura de receber um atk super efetivo de uma criatura de 2 atributos {'_'*26} ", 
    "valor_do_efeito" : 0, 
    "comando_uso_item" : 3,
    "idioma": 2, 
    "item_capshop_plus": 0
}]

_itens_capshop_plus = [{
    "tipo_capshop": 1, 
    "id_item_capshop": '1+', 
    "nome":"Capchance+", 
    "abreviacao":"chance+",
    "custo_em_capcoins":80, 
    "descricao": f"increase more the capture chance {'_'*24} ", 
    "valor_do_efeito" : 10, 
    "comando_uso_item" : 2,
    "idioma": 1, 
    "item_capshop_plus": 1
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '1+', 
    "nome":"Capchance+", 
    "abreviacao":"chance+",
    "custo_em_capcoins":80, 
    "descricao": f"aumenta mais a chance de captura {'_'*22} ", 
    "valor_do_efeito" : 10, 
    "comando_uso_item" : 2,
    "idioma": 2, 
    "item_capshop_plus": 1
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '2+', 
    "nome":"Capspecial+", 
    "abreviacao":"special+",
    "custo_em_capcoins":120, 
    "descricao": f"increase more the Special chance {'_'*24} ", 
    "valor_do_efeito" : 10, 
    "comando_uso_item" : 2,
    "idioma": 1, 
    "item_capshop_plus": 1
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '2+', 
    "nome":"Capspecial+", 
    "abreviacao":"special+",
    "custo_em_capcoins":120, 
    "descricao": f"aumenta mais a chance de Especial {'_'*22} ", 
    "valor_do_efeito" : 10, 
    "comando_uso_item" : 2,
    "idioma": 2, 
    "item_capshop_plus": 1
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '4+', 
    "nome":"Capevol+", 
    "abreviacao":"capevol+",
    "custo_em_capcoins":50, 
    "descricao": f"Evolve an able creature to a specific stage {'_'*21} ", 
    "valor_do_efeito" : 0, 
    "comando_uso_item" : 1,
    "idioma": 1, 
    "item_capshop_plus": 0
},{
    "tipo_capshop": 1, 
    "id_item_capshop": '4+', 
    "nome":"Capevol+", 
    "abreviacao":"capevol+",
    "custo_em_capcoins":50, 
    "descricao": f"Evolui uma criatura apta para um estágio específico {'_'*7} ", 
    "valor_do_efeito" : 0, 
    "comando_uso_item" : 1,
    "idioma": 2, 
    "item_capshop_plus": 0
}]

dados_padrao_tabela_itens_capshop = lambda dados = {} : _itens_capshop + _itens_capshop_plus