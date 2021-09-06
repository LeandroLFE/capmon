script_insert_table_hordas_canal = lambda dados = {} : f"""
    INSERT INTO Hordas_{dados["canal_id"]} (tipo_horda, horda_ativa) 
    VALUES (1, 0);
"""

script_update_table_hordas_tipo_horda_canal = lambda dados = {} : f"""
    UPDATE Hordas_{dados["canal_id"]} 
    SET tipo_horda = (
        SELECT id 
        FROM Tipo_hordas_{dados["canal_id"]}
        WHERE percent_atual = 100
        ORDER BY prioridade DESC
        LIMIT 1
    )
    ; 
"""

script_update_table_hordas_horda_ativa_canal = lambda dados = {} : f"""
    UPDATE Hordas_{dados["canal_id"]} 
    SET horda_ativa = :horda_ativa
"""