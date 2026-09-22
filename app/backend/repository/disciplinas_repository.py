from sqlalchemy import text
from .base_repository import BaseRepository as BR
from typing import Any


class DisciplinaRepository(BR):

    def insert(self, data: dict[Any]) -> None:
        stmt = text("""
        INSERT INTO disciplinas
        (
            nome_disciplina,
            fk_formato_disciplina,
            carga_horaria_disciplina,
            horario_inicio_disciplina,
            horario_termino_disciplina,
            pratica_disciplina,
            especialidade_necessaria_disciplina
        )
        VALUES
        (
            :nome_disciplina,
            :fk_formato_disciplina,
            :carga_horaria_disciplina,
            :horario_inicio_disciplina,
            :horario_termino_disciplina,
            :pratica_disciplina,
            :especialidade_necessaria_disciplina
        );""")
        self.execute_and_commit_db_query(stmt, data)

    def select(self) -> list[tuple]:
        stmt = text("""
        SELECT
            d.id_disciplina,
            d.nome_disciplina,
            d.fk_formato_disciplina,
            f.nome_formato,
            d.carga_horaria_disciplina,
            d.horario_inicio_disciplina,
            d.horario_termino_disciplina,
            d.pratica_disciplina,
            d.especialidade_necessaria_disciplina
        FROM
            disciplinas AS d
        LEFT JOIN formato AS f ON f.id_formato = d.fk_formato_disciplina;
        """)
        return self.execute_db_query(stmt)

    def update(self, data: dict[Any], id: int) -> None:
        stmt = text("""
        UPDATE disciplinas
            SET nome_disciplina = :nome,
                fk_formato_disciplina = :formato,
                carga_horaria_disciplina = :carga_horaria,
                horario_inicio_disciplina = :horario_inicio,
                horario_termino_disciplina = :horario_termino,
                pratica_disciplina = :pratica,
                especialidade_necessaria_disciplina = :especialidade
            WHERE
                id_disciplina = :id,
            """)
        self.execute_and_commit_db_query(stmt, data, id)

    def delete(self, id: int) -> None:
        stmt = text("""DELETE FROM disciplinas WHERE id = :id;""")
        self.execute_and_commit_db_query(stmt, None, id)
