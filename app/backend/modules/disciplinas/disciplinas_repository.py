from sqlalchemy import text
from base_repository import BaseRepository as BR
from typing import Any


class DisciplinaRepository(BR):

    def insert(self, data: list[tuple]):
        stmt = text("""
        INSERT INTO disciplinas
        (
            nome,
            fk_formato,
            carga_horaria,
            horario_inicio,
            horario_termino,
            pratica,
            especialidade_necessaria
        )
        VALUES
        (
            :nome,
            :fk_formato,
            :carga_horaria,
            :horario_inicio,
            :horario_termino,
            :pratica
        );""")
        print(self.execute_and_commit_db_query(stmt, data))

    def select(self) -> list[tuple]:
        stmt = text("""
        SELECT
            d.id,
            d.nome,
            d.fk_formato,
            f.nome_formato,
            d.carga_horaria,
            d.horario_inicio,
            d.horario_termino,
            d.pratica
        FROM
            disciplinas AS d
        LEFT JOIN formato AS f ON f.id_formato = d.fk_formato;
        """)
        return self.execute_db_query(stmt)

    def update(self, data: dict[Any], id: int) -> None:
        stmt = text("""
        UPDATE disciplinas
            SET nome = :nome,
                fk_formato = :formato,
                carga_horaria = :carga_horaria,
                horario_inicio = :horario_inicio,
                horario_termino = :horario_termino,
                pratica = :pratica
            WHERE
                id = :id
            """)
        self.execute_and_commit_db_query(stmt, data, id)

    def delete(self, id: int) -> None:
        stmt = text("""DELETE FROM disciplinas WHERE id = :id;""")
        self.execute_and_commit_db_query(stmt, None, id)
