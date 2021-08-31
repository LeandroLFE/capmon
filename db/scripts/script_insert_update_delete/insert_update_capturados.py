'''
Requer: {
   "id_criatura" : int,  
   "canal_id" : str,
   "aventureiro_id" : str,
   "cp_inicial" : int,
   "golpe": int (atributo),
   "especial" : int (0 ou 1),
   "percent_update_cp" : float (padrão 0.1),
   "cp" : int,
   "cp_limite" : int
}
'''
update_capturados = lambda dados = {} : f"""
    INSERT INTO Capturados_{dados["canal_id"]} (id_criatura, aventureiro_id, cp, golpe, especial, cont_capturados, origem) 
    VALUES (:id_criatura, :aventureiro_id, :cp_inicial, :golpe, :especial, 1, :id_criatura) 
    ON DUPLICATE KEY 
    UPDATE 
    cp = if(cp + :percent_update_cp * :cp >= :cp_limite, :cp_limite, cp + :percent_update_cp * :cp), 
    golpe = :golpe, especial = if (especial = '1', '1', :especial), 
    cont_capturados = (cont_capturados + 1)
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

