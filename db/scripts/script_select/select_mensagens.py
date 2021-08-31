'''
Requer:{
    "canal_id" : text
}
'''

select_ultima_msg = lambda dados = {} : """
    SELECT msg
    FROM Mensagens
    WHERE Canal_ID = :canal_id 
"""