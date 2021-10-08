-- SQLite
SELECT Criaturas.id, Capturados.aventureiro_id, Capturados.cp, 
    Criaturas.evolucao, Criaturas.forma, Criaturas.linha_evolutiva, Criaturas.evolui, Capturados.origem, 
    Criaturas.cp_min, Criaturas.cp_max,  
    Atr1.nome AS "nome_atributo1",
    Atr2.nome AS "nome_atributo2", 
    Pc.chance_captura, 
    Pc.chance_especial,
    Criaturas.Nome, Criaturas.tipo, Criaturas.CP_limite, 
    Atrgolpe.nome as "golpe", Capturados.especial, Criaturas.custo 
    FROM Criaturas 
    INNER JOIN Parametros_criaturas as Pc 
    ON Criaturas.parametro_criatura = Pc.id
    INNER JOIN
    (
    SELECT Atributos.nome, Atributos.ref, Atributos.tipo, Idiomas.nome as nome_idioma_atr1
    FROM Atributos 
    INNER JOIN Idiomas 
    ON Atributos.idioma = Idiomas.id
    ) AS Atr1
    ON Criaturas.atributo1 = Atr1.ref 
    AND Criaturas.tipo = Atr1.tipo 
    LEFT JOIN 
    (
    SELECT Atributos.nome, Atributos.ref, Atributos.tipo, Idiomas.nome as nome_idioma_atr2
    FROM Atributos 
    INNER JOIN Idiomas 
    ON Atributos.idioma = Idiomas.id
    ) AS Atr2
    ON criaturas.atributo2 = Atr2.ref 
    AND criaturas.tipo = Atr2.tipo 
    INNER JOIN Capturados_178959532 as Capturados 
    ON Criaturas.id = Capturados.id_criatura
    INNER JOIN 
    (
        SELECT Atributos.nome, Atributos.ref, Atributos.tipo, Idiomas.nome as nome_idioma_golpe
        FROM Atributos
        INNER JOIN Idiomas 
        ON Atributos.idioma = Idiomas.id
    )   AS Atrgolpe
    ON Capturados.Golpe = Atrgolpe.ref 
    WHERE aventureiro_id = '178959532'
    AND Criaturas.nome = 'pikachu'