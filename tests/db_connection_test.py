from app.backend.core.interface import engine_mysql
from sqlalchemy import text
from dotenv import load_dotenv
import os

load_dotenv()

database = os.getenv("MYSQL_DATABASE")
partial_database = database.split('_')[0]

def teste_conexao_bd():
    with engine_mysql.connect() as conn:
        result = conn.execute(text(f"select Db from mysql.db where Db like '{partial_database}%';"))

    for row in result:
        row_array = str(row).strip("(',')").split("\\")
        row_treated = row_array[0] + row_array[2]
        assert row_treated == database
