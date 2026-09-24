from sqlalchemy import text
from ..base_repository import BaseRepository as BR


class FormatoRepository(BR):

    def insert(self, data: list[tuple]) -> None:
        stmt = text("""INSERT INTO formatos
        (
            nome
        )
        VALUES
        (
            :nome
        );""")
        print(self.execute_and_commit_db_query(stmt, data))

    def select(self) -> list[tuple]:
        stmt = text("""
            SELECT id, nome FROM formatos;
        """)
        return self.execute_db_query(stmt)

    def update(self, data: list[tuple], id: int) -> None:
        stmt = text("""UPDATE formatos SET nome = :nome WHERE id = :id;""")
        self.execute_and_commit_db_query(stmt, data, id)

    def delete(self, id: int) -> None:
        stmt = text("""DELETE FROM formatos WHERE id = :id;""")
        self.execute_and_commit_db_query(stmt, id)
