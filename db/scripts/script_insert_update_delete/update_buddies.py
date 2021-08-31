'''
Requer: {
    "canal_id" : str,
    "novo_id":int,
    "id_criatura": int,
    "aventureiro_id" : str
}
'''

update_buddy_evolui = lambda dados : f"""
    UPDATE capturados_{dados["canal_id"]}
    SET id_criatura = :novo_id
    WHERE aventureiro_id = :aventureiro_id
    AND ID_criatura = :id_criatura 
"""

'''
Requer: {
    "canal_id" : str,
    "aventureiro_id" : str,
    "id_criatura": int
}
'''

update_buddy_troca = lambda dados : f"""
    INSERT INTO buddies_{dados["canal_id"]} (Aventureiro_index, ID_criatura)
    VALUES (:aventureiro_id, :id_criatura) 
    ON DUPLICATE KEY 
    UPDATE 
    ID_criatura = :id_criatura
    Cont_hordas_buddy = 0 
"""

'''
Requer: {
    "canal_id" : str,
    "numero_hordas" : int,
    "aumento_cp": int,
    "aventureiros_index" : int,
}
'''

update_buddy_cont_hordas = lambda dados = {} : f"""
    UPDATE capturados_{dados["canal_id"]} as capturados 
    Inner join ( 
    criaturas 
    INNER JOIN ( 
    aventureiros_{dados["canal_id"]} as aventureiros 
    INNER JOIN buddies_{dados["canal_id"]} as buddies 
    ON buddies.aventureiro_id = aventureiros.aventureiro_id 
    ) 
    ON buddies.id_criatura = criaturas.num 
    ) 
    ON capturados.ID_criatura = buddies.id_criatura 
    AND capturados.aventureiro_id = aventureiros.aventureiro_id 
    SET capturados.CP = if(Cont_hordas_buddy + 1 >= :numero_hordas, 
    IF(capturados.CP + :aumento_cp > criaturas.CP_limite, criaturas.CP_limite, 
    capturados.CP + :aumento_cp), Capturados.CP), 
    Cont_hordas_buddy = if(Cont_hordas_buddy +1 >= :numero_hordas, 0, Cont_hordas_buddy + 1) 
    WHERE buddies.Aventureiro_index IN :aventureiros_index   
"""

'''
Requer: {
    "canal_id" : str,
    "aumento_cp" : int,
    "aventureiros_index" : int,
}
'''

update_buddy_cp = lambda dados : f"""
    UPDATE capturados_{dados["canal_id"]} as capturados 
    Inner join ( 
    criaturas 
    INNER JOIN ( 
    aventureiros_{dados["canal_id"]} as aventureiros 
    INNER JOIN buddies_{dados["canal_id"]} as buddies 
    ON buddies.aventureiro_id = aventureiros.aventureiro_id 
    ) 
    ON buddies.id_criatura = criaturas.num 
    ) 
    ON capturados.ID_criatura = buddies.id_criatura 
    AND capturados.aventureiro_id = aventureiros.aventureiro_id 
    SET capturados.CP = IF(
        capturados.CP + :aumento_cp > criaturas.CP_limite, 
        criaturas.CP_limite, capturados.CP + :aumento_cp
    )
    WHERE buddies.Aventureiro_index = :aventureiros_index " 
"""