from logging import basicConfig
from utils.blender_bcolors import bcolors
config = lambda dados : {
        'version': 1,
        'formatters': {
            'console': {
                'class': 'logging.Formatter',
                'format': f'{bcolors.WARNING}%(threadName)s %(processName)s %(asctime)s {bcolors.FAIL}{bcolors.BOLD}%(levelname)s{bcolors.WARNING} %(name)s{bcolors.ENDC}\n%(message)s\n'
            },
            'file': {
                'class': 'logging.Formatter',
                'format': '%(threadName)s %(processName)s %(asctime)s %(levelname)s %(name)s\n%(message)s\n'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'console',
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': f"{dados['filename']}.log",
                'mode': 'a',
                'formatter': 'file',
                'level': 'INFO',
                'encoding' : 'UTF-8',
            },
            'errors': {
                'class': 'logging.FileHandler',
                'filename': 'logs/bot-errors.log',
                'mode': 'a',
                'level': 'ERROR',
                'formatter': 'file',
                'encoding' : 'UTF-8',
            },
        },
        'loggers': {
            'bot': {
                'handlers': ['console', 'file']
            }
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['console', 'file', 'errors']
        },
    }