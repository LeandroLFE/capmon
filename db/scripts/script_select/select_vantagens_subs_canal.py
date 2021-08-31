'''
Requer: {
    "canal_id" : str
}
'''
select_vantagens_subs_canal = lambda dados = "" : """
    Select Vsp.habilita_vantagens_subs, Vsp.aumento_chance_captura, 
    Vsp.aumento_chance_especial, Vsp.acesso_exclusivo_capshop
    FROM Canais
    INNER JOIN Vantagens_subs_perfis as Vsp
    ON Canais.perfil_vantagens_subs = Vsp.id
    WHERE canal_id = :canal_id
"""

