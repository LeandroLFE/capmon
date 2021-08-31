'''
Requer: {
    "canal_id" : str
}
'''

delete_canais_id = lambda dados = {} : """
    DELETE FROM Canais WHERE canal_id = :canal_id;
"""