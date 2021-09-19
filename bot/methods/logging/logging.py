from logging import getLogger
from logging.config import dictConfig
from bot.methods.logging.config import config

def new_logging(canal_id):
    _nome_arquivo = f"logs/bot_{canal_id}"
    log_config = config({"filename":_nome_arquivo})
    dictConfig(log_config)
    return getLogger(_nome_arquivo)