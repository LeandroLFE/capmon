'''
Requer: {
   "id_criatura" : int,  
   "canal_id" : str,
   "aventureiro_id" : str,
   "cp" : int,
   "golpe": int (atributo),
   "especial" : int (0 ou 1),
   "percent_update_cp" : float (padrão 0.1),
   "cp" : int,
   "cp_limite" : int
}
'''
script_insert_update_capturados = lambda dados = {} : f"""
    INSERT INTO Capturados_{dados["canal_id"]} (id_criatura, aventureiro_id, cp, golpe, especial, origem) 
    VALUES (:id_criatura, :aventureiro_id, :cp, (
        SELECT id 
        FROM Atributos
        WHERE LOWER(nome) = LOWER(:golpe)
    ), :especial, :id_criatura) 
    ON CONFLICT(id_criatura, aventureiro_id) DO 
    UPDATE 
    SET cp = :cp, 
    golpe = (
        SELECT id 
        FROM Atributos
        WHERE LOWER(nome) = LOWER(:golpe)
    ), 
    especial = CASE WHEN especial = 1 THEN 1 ELSE :especial END
    WHERE aventureiro_id = :aventureiro_id
    AND id_criatura = :id_criatura
"""

'''
Requer: {
    "novo_id" : int,
    "id_criatura": int,
    "aventureiro_id" : str
}
'''

update_evolui_capturado = lambda dados = {} : f"""
    UPDATE Capturados_{dados["canal_id"]}
    SET id_criatura = :novo_id
    WHERE aventureiro_id = :aventureiro_id
    AND ID_criatura = :id_criatura  
"""
'''
Requer: {
   "id_criatura" : int,  
   "aventureiro_id" : str,
   "cp_inicial" : int,
   "golpe": int (atributo),
   "especial" : int (0 ou 1),
   "percent_update_cp" : float (padrão 0.1),
   "cp" : int,
   "cp_limite" : int
}
'''

update_devolui_capturado = lambda dados : f"""
    UPDATE Capturados_{dados["canal_id"]} 
    SET id_criatura = :origem
    CP = :cp_inicial, 
    Golpe = ( 
    SELECT atributo1 
    FROM Criaturas 
    Where num = :id_criatura
    ) 
    WHERE aventureiro_id = :aventureiro_id
    AND ID_criatura = :id_criatura
"""

