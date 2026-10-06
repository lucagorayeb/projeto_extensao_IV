from ..base_repository import BaseRepository as BR


class FormatoRepository(BR):

    def insert(self, data: dict) -> None:
        stmt = "insert into formato (nome) values (:nome);"
        self.execute_and_commit_db_query(stmt=stmt, data=data)

    def select(self) -> object | None:
        stmt = "select id, nome from formato;"
        return self.execute_db_query(stmt=stmt)

    def update(self, data: dict) -> None:
        stmt = "update formato set nome = :nome where id = :id;"
        self.execute_and_commit_db_query(stmt=stmt, data=data)

    def delete(self, data: dict) -> None:
        stmt = "delete from formato where id = :id;"
        self.execute_and_commit_db_query(stmt=stmt, data=data)

    def select_by_id(self, data: dict) -> object | None:
        stmt = "select id, nome from formato where id = :id;"
        return self.execute_db_query(stmt=stmt, data=data)
