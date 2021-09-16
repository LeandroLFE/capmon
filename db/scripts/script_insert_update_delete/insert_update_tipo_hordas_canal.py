script_insert_table_tipo_hordas_canal = lambda dados = {} : f"""
    INSERT INTO Tipo_hordas_{dados["canal_id"]} (id, nome, prioridade, percent_atual) 
    VALUES (:tipo_horda_id, :nome_horda, :prioridade, :percent_atual);
"""

script_update_table_tipo_hordas_reset_percent_atual = lambda dados = {} : f"""
    UPDATE Tipo_hordas_{dados["canal_id"]} 
    SET percent_atual = 0
    WHERE percent_atual = 100
    AND prioridade > 0
    AND prioridade <= (
        SELECT prioridade
        FROM Tipo_hordas_{dados["canal_id"]}   
        WHERE percent_atual = 100
        ORDER BY prioridade DESC
        LIMIT 1
    );
"""


script_update_table_tipo_hordas_elemental_canal = lambda dados = {} : f"""
    UPDATE Tipo_hordas_{dados["canal_id"]} 
    SET percent_atual = 
    CASE WHEN 
        percent_atual + (
        SELECT incremento_para_horda_elemental
        FROM Canais
        INNER JOIN Parametros_hordas as Ph
        ON Canais.parametros_hordas = Ph.id
        WHERE Canais.canal_id = :canal_id
        ) > 100 
    THEN 100 
    ELSE 
        percent_atual + (
        SELECT incremento_para_horda_elemental
        FROM Canais
        INNER JOIN Parametros_hordas as Ph
        ON Canais.parametros_hordas = Ph.id
        WHERE Canais.canal_id = :canal_id
    )
    END
    WHERE prioridade = 1
    ; 
"""

script_update_table_tipo_hordas_capraid_canal = lambda dados = {} : f"""
    UPDATE Tipo_hordas_{dados["canal_id"]} 
    SET Percent_atual = 
    CASE WHEN 
        percent_atual + (
        SELECT Incremento_para_capraid
        FROM Canais
        INNER JOIN Parametros_hordas as Ph
        ON Canais.parametros_hordas = Ph.id
        WHERE Canais.canal_id = :canal_id
        ) > 100 
    THEN 100 
    ELSE 
        Percent_atual + (
        SELECT Incremento_para_capraid
        FROM Canais
        INNER JOIN Parametros_hordas as Ph
        ON Canais.parametros_hordas = Ph.id
        WHERE Canais.canal_id = :canal_id
        )
    END
    WHERE Prioridade = 2
    ; 
"""

script_update_table_tipo_hordas_horda_especifica_canal = lambda dados = {} : f"""
    UPDATE Tipo_hordas_{dados["canal_id"]} 
    SET Percent_atual = 100
    WHERE Prioridade = 3
    ; 
"""