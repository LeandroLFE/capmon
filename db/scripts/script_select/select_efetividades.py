# Requer atributo e atributo_comp = {"atributo": int (id_atributo), "atributo_comp" : int (id_atributo)}
select_efetividades = lambda : """
    Select fator 
    FROM efetividades 
    WHERE atributo = :atributo 
    AND atributo_comp = :atributo_comp
"""