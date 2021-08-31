script_select_todos_idiomas = lambda dados = {}: """
    SELECT DISTINCT nome from Idiomas;
"""

'''
Requer {
    "nome_idioma" : str
}
'''

script_select_idioma_por_nome = lambda dados = {}: """
    SELECT nome FROM Idiomas WHERE nome = :nome_idioma
"""