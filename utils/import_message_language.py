from importlib import import_module
from typing import Iterable

def import_message_language_all(idiomas : Iterable, 
    resource_foulder: str, resource_file: str, resource_name : str, 
    parameters : dict):
    
    messages = []
    for idioma in idiomas:
        if issubclass(type(idioma), Iterable):
            _messages = getattr(import_module(f"bot.cogs.messages.{idioma[0]}.{resource_foulder}.{resource_file}"), resource_name)
        elif type(idioma) == str:
            _messages = getattr(import_module(f"bot.cogs.messages.{idioma}.{resource_foulder}.{resource_file}"), resource_name)
        else:
            raise Exception(f"Tipo de Idioma inválido: {type(idioma)}" )
        
        messages += [_messages(parameters)]

    return messages

def import_message_language_by_one(idioma : Iterable or str, 
    resource_foulder: str, resource_file: str, resource_name : str, 
    parameters : dict):

    if type(idioma) == str:
        _messages = getattr(import_module(f"bot.cogs.messages.{idioma}.{resource_foulder}.{resource_file}"), resource_name)
    elif issubclass(type(idioma), Iterable):
        _messages = getattr(import_module(f"bot.cogs.messages.{idioma[0]}.{resource_foulder}.{resource_file}"), resource_name)
    else:
        raise Exception(f"Tipo de Idioma inválido: {type(idioma)}" )
    
    messages = _messages(parameters)

    return messages
