'''
Requer: {
    "aventureiro" : str
}
'''
capmon_channel_messages_normal = lambda dados : {
    "start" : f'Olá {dados["aventureiro"]}, Capaventura iniciada no seu canal!',
    "stop" : f'Olá {dados["aventureiro"]}, partindo do seu canal, até a próxima Capaventura!',
    "language" : f'Idioma pt-br selecionado {dados["aventureiro"]}',
}

'''
Requer: {
    "aventureiro" : str,
    "idiomas" : list,
    "comandos" : list
}
'''

capmon_channel_messages_error = lambda dados : {
    "start" : f'{dados["aventureiro"]}, a Capaventura já se encontra ativa no seu canal!',
    "stop_inactive" : f'{dados["aventureiro"]}, Não é possível parar uma Capaventura em um canal inativo!',
    "stop_not_start" : f'{dados["aventureiro"]}, Não é possível parar uma Capaventura que ainda não foi iniciada!',
    "language_invalid" : f'Idioma inválido {dados["aventureiro"]}. Disponíveis: {dados["idiomas"]}',
    "language_inactive" : f'{dados["aventureiro"]}, Não é possível mudar o idioma de uma Capaventura inativa!',
    "language_stop" : f'{dados["aventureiro"]}, Não é possível mudar o idioma de uma Capaventura que ainda não foi iniciada!',
    "invalid_command" : f'{dados["aventureiro"]}, Comando inválido, disponíveis:{dados["comandos"]}!'
}