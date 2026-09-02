from sqlalchemy import text
from interface import engine


def insert_into_db_disciplinas(item: str) -> None:
    with engine.connect() as con:
        stmt = text("""INSERT INTO disciplinas
        (
            disciplina,
            fk_formato_disciplina
        )
        VALUES
        (
            :item
        );""")
        con.execute(stmt, {'item': item})
        con.commit()


def select_formatos_from_bd() -> list[tuple]:
    with engine.connect() as con:
        stmt = text(
            """SELECT
                id,
                disciplina,
                fk_formato_disciplina
            FROM
                disciplinas;"""
        )
        return con.execute(stmt)
