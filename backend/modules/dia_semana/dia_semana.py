from backend.core.interface import engine_mysql, metadata
from sqlalchemy import Table

dia_semana = Table(
    "dia_semana",
    metadata,
    autoload_with=engine_mysql
)