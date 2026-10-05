from ..base_repository import BaseRepository as Br


class EspecialidadeRepository(Br):

    def insert(self, data: dict) -> None:
        stmt = "insert into especialidade (nome) values (:nome);"
        self.execute_and_commit_db_query(stmt=stmt, data=data)

    def select(self) -> list[dict] | None:
        stmt = "select id, nome from especialidade;"
        return self.execute_db_query(stmt=stmt)

    def update(self, data: dict) -> None:
        stmt = "update especialidade set nome = :nome where id = :id;"
        self.execute_and_commit_db_query(stmt=stmt, data=data)

    def delete(self, data: dict) -> None:
        stmt = "delete from especialidade where id = :id;"
        self.execute_and_commit_db_query(stmt=stmt, data=data)

    def select_by_id(self, data: dict) -> list[dict] | None:
        stmt = "select id, nome from especialidade where id = :id;"
        return self.execute_db_query(stmt=stmt, data=data)