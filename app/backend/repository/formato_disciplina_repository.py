from sqlalchemy import text
from interface import engine


def insert_into_db_formato_disciplina(item: str) -> None:
    with engine.connect() as con:
        stmt = text("""INSERT INTO formato_disciplina
        (
            formato_disciplina
        )
        VALUES
        (
            :item
        );""")
        con.execute(stmt, {'item': item})
        con.commit()


def select_formatos_from_bd() -> list[tuple]:
    with engine.connect() as con:
        stmt = text("SELECT id, formato_disciplina FROM formato_disciplina;")
        return con.execute(stmt)
