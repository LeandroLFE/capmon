'''
Requer: {
    "aventureiro" : str
}
'''
capmon_channel_messages_normal = lambda dados : {
    "start" : f'Hello {dados["aventureiro"]}, the Capadventure has been started in your channel!',
    "restart": f'Hello {dados["aventureiro"]}, the Capadventure has been restarted in your channel!',
    "stop" : 'The Capadventure has finished, leaving from your channel, hope you come back soon',
    "language" : f'English language has been selected {dados["aventureiro"]}',
}

'''
Requer: {
    "aventureiro" : str,
    "idiomas" : list,
    "comandos" : list
}
'''
capmon_channel_messages_error = lambda dados : {
    "start" : f'{dados["aventureiro"]},  the Capadventure is already active in your channel!',
    "stop_inactive" : f'{dados["aventureiro"]}, It´s not possible to stop an Capadventure in an inactive channel!',
    "stop_not_start" : f'{dados["aventureiro"]}, It´s not possible to stop an Capadventure that it´s been not started yet',
    "language_invalid" : f'Invalid language {dados["aventureiro"]}. Available: {dados["idiomas"]}',
    "language_inactive" : f'{dados["aventureiro"]}, It´s not possible to change the language in an inactive Capadventure!',
    "language_stop" : f'{dados["aventureiro"]}, It´s not possible to change the language in an Capadventure that it´s been not started yet!',
    "invalid_command" : f'{dados["aventureiro"]}, Invalid command, available:{dados["comandos"]}!'
}