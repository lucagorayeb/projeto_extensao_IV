from sqlalchemy import (
    create_engine,
    URL
)
import os
from dotenv import load_dotenv

load_dotenv()

# Conexão com o SQLITE
engine_sqlite = create_engine(
    "sqlite+pysqlite:///database/ensalamento.sqlite",
    echo=False
)

# Conexão com o MySQL
url_object = URL.create(
    "mysql+pymysql",
    username=os.getenv("MYSQL_ROOT_USER"),
    password=os.getenv("MYSQL_ROOT_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=os.getenv("MYSQL_PORT"),
    database=os.getenv("MYSQL_DATABASE")
)

engine_mysql = create_engine(url_object, echo=False)
