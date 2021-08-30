from auth.auth import db_location, db_name
from db.connect.db_classes.conectaAioSqlite import ConectaAioSQLite

atualDB = ConectaAioSQLite(f"{db_location}{db_name}")