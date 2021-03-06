'''
Requer: {
    "canal_id" : str
}
'''
select_parametros_gerais_canal = lambda dados = "" : """
    Select Pg.tamanho_max_msgs, Pg.tempo_sessao_capshop, Pg.tempo_sessao_capmon, 
    Pg.tempo_espera_obter_capmove, Pg.tempo_capbattle, Pg.cooldown_capbattle
    FROM Canais
    INNER JOIN Parametros_gerais as Pg
    ON Canais.parametros_gerais = Pg.id
    WHERE Canais.canal_id = :canal_id
"""

'''
Requer: {
    "canal_id" : str
}
'''
select_parametros_capboard_canal = lambda dados = "" : """
    Select Pc.add_vitoria, Pc.add_derrota, Pc.add_empate,
    Pc.capcoins_primeiro, Pc.capcoins_segundo, Pc.capcoins_terceiro
    FROM Canais
    INNER JOIN Parametros_capboard as Pc
    ON Canais.parametros_capboard = Pc.id
    WHERE Canais.canal_id = :canal_id
"""

'''
Requer: {
    "canal_id" : str
}
'''
select_parametros_buddies_canal = lambda dados = "" : """
    Select Pb.qtde_hordas_para_add_cp, Pb.add_cp_min, Pb.add_cp_max
    FROM Canais
    INNER JOIN Parametros_buddies as Pb
    ON Canais.parametros_buddies = Pb.id
    WHERE Canais.canal_id = :canal_id
"""



select_parametros_aventureiros_novo_canal = lambda dados = "" : """
    Select Pa.capcoins_iniciais, Pa.cont_hordas_para_add_capcoins, Pa.cont_sequencia_para_add_capcoins_bonus, 
    Pa.add_capcoins_min, Pa.add_capcoins_max, 
    Pa.add_capcoins_bonus_min, Pa.add_capcoins_bonus_max 
    FROM Parametros_aventureiros as Pa
    ORDER BY Pa.id
    LIMIT 1;
"""


'''
Requer: {
    "canal_id" : str
}
'''
select_parametros_aventureiros_canal = lambda dados = "" : """
    Select Pa.capcoins_iniciais, Pa.cont_hordas_para_add_capcoins, Pa.cont_sequencia_para_add_capcoins_bonus, 
    Pa.add_capcoins_min, Pa.add_capcoins_max, 
    Pa.add_capcoins_bonus_min, Pa.add_capcoins_bonus_max 
    FROM Canais
    INNER JOIN Parametros_aventureiros as Pa
    ON Canais.parametros_aventureiros = Pa.id
    WHERE Canais.canal_id = :canal_id
"""

'''
Requer: {
    "criatura_nome" : str
}
'''
select_parametros_criatura = lambda dados = "" : """
    Select Pc.cp_inicial, Pc.chance_captura, Pc.chance_especial, Pc.num_tentativas_caso_zero_ou_negativo
    FROM Parametros_criaturas as Pc
    INNER JOIN Criaturas
    ON Pc.id = Criaturas.parametro_criatura
    WHERE LOWER(Criaturas.nome) = LOWER(:criatura_nome)
"""

'''
Requer: {
    "canal_id" : str
}
'''
select_parametros_hordas_canal = lambda dados = "" : """
    Select Ph.incremento_para_horda_elemental, Ph.incremento_para_capraid,
    Ph.tempo_horda_min, Ph.tempo_horda_max, 
    Ph.tempo_entre_hordas_min, Ph.tempo_entre_hordas_max, 
    Ph.aviso_horda_terminando_em_x_segundos,
    Ph.faixa_pessoas_live_pequeno, Ph.fator_cp_boss_capraid_live_pequeno_percent, 
    Ph.faixa_pessoas_live_medio, Ph.fator_cp_boss_capraid_live_medio_percent, 
    Ph.faixa_pessoas_live_grande, Ph.fator_cp_boss_capraid_live_grande_percent,
    Ph.fator_cp_boss_capraid_live_muito_grande_percent 
    FROM Canais
    INNER JOIN Parametros_hordas as Ph
    ON Canais.parametros_hordas = Ph.id
    WHERE Canais.canal_id = :canal_id
"""
