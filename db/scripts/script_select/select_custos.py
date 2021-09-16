select_all_ref_custos = lambda dados = {}: """
    SELECT Distinct ref
    FROM Custos
    WHERE nome <> 'n/a' 
"""