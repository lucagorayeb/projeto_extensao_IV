from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

# Conexão com o SQLITE
engine_sqlite = create_engine(
    "sqlite+pysqlite:///database/ensalamento.sqlite",
    echo=False
)

# Conexão com o MySQL
usuario = os.getenv("MYSQL_USER")
senha = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
porta = os.getenv("MYSQL_PORT")
banco = os.getenv("MYSQL_DATABASE")

string_conexao_mysql = f"""
    mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}"""

engine_mysql = create_engine(string_conexao_mysql)
