# from sqlalchemy import text
from .base_repository import BaseRepository as BR


class DisciplinaRepository(BR):

    def insert(self, item: str) -> None:
        # stmt = text("""
        # INSERT INTO disciplinas
        # (
        #     disciplina,
        #     fk_formato_disciplina
        # )
        # VALUES
        # (
        #     :item
        # );""")
        # data = {'item': item}
        # self.execute_and_commit_db_query(stmt, data)
        print("Chegou até a função insert da tabela disciplina.")

    def select(self) -> list[tuple]:
        # stmt = text("""
        # SELECT
        #     id,
        #     disciplina,
        #     fk_formato_disciplina
        # FROM
        #     disciplinas;""")
        # return self.execute_db_query(stmt)
        print("Chegou até a função select da tabela disciplina.")

    def update(self, data: dict, id: int) -> None:
        print("Chegou até a função update da tabela disciplina.")

    def delete(self, id: int) -> None:
        print("Chegou até a função delete da tabela disciplina.")
