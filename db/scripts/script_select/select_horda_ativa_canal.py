select_horda_ativa_canal = lambda dados ={} : f"""
    SELECT Tipo_hordas.nome 
    FROM Hordas_{dados["canal_id"]} as Hordas
    INNER JOIN Tipo_hordas_{dados["canal_id"]} as Tipo_hordas
    ON Hordas.tipo_horda = Tipo_hordas.id
    WHERE horda_ativa = 1
"""