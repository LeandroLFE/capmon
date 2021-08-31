'''
Requer {
    "canal_id" : text,
    "msg" : text
}
'''
script_insert_msg = lambda dados = {}: """
    INSERT INTO Mensagens (canal_id, msg) 
    VALUES (:canal_id, :msg)
"""

'''
Requer : {
    "canal_id" : text,
    "msg" : text
}
'''

script_update_msg = lambda dados = {} : """
    UPDATE Mensagens 
    SET msg = :msg
    WHERE canal_id = :canal_id 
"""