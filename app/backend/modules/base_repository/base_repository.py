from typing import Any
from app.backend.core.interface import engine_mysql as eng
from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    def execute_db_query(
            self,
            stmt: str,
            data: dict = None,
            id: int = None) -> Any:
        with eng.connect() as conn:
            return conn.execute(stmt, data, id)

    def execute_and_commit_db_query(self,
                                    stmt: str,
                                    data: list[tuple] = None,
                                    id: int = None) -> None:
        with eng.connect() as conn:
            conn.execute(stmt, data, id)
            conn.commit()
