from os import getenv
from dotenv import load_dotenv

load_dotenv()
client_id = getenv('CLIENT_ID')
client_secret = getenv('CLIENT_SECRET')
token = getenv('OAUTH_TOKEN')
nick = getenv('BOT_USERNAME')
db_name = getenv('DB_NAME')
db_location = getenv('DB_LOCATION')
prefix = '!'
initial_channels = ["capmon"]