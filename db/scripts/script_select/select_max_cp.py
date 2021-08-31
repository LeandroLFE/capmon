select_max_cp = lambda canal : f"""
    SELECT max capturados.CP 
    FROM capturados_{canal}
"""