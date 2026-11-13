from backend.modules.base_repository import BaseRepository
from sqlalchemy import insert, update, delete, select
from backend.modules.professor.professor_model import Professor
from backend.modules.disciplina.disciplina_model import Disciplina
from backend.modules.sala.sala_model import Sala


class TurmaRepository(BaseRepository):

    def insert(self, data: dict) -> None:
        pass

    def update(self, data: dict) -> None:
        pass

    def delete(self, id: int) -> None:
        pass

    def select(self) -> list:
        pass