from typing import Any
from app.backend.core.interface import engine
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

    def execute_db_query(self, stmt: str, data: dict = None) -> Any:
        with engine.connect() as conn:
            return conn.execute(stmt, data)

    def execute_and_commit_db_query(self,
                                    stmt: str,
                                    data: dict = None) -> None:
        with engine.connect() as conn:
            conn.execute(stmt, data)
            conn.commit()
