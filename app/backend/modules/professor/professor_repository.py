from ..base_repository import BaseRepository
from sqlalchemy import insert, update, delete, select
from .professor_model import Professor
from .professor_dto import ProfessorDTO

class ProfessorRepository(BaseRepository):

    def insert(self, data: ProfessorDTO) -> None:
        stmt = insert(
            Professor
        ).values(
            nome = data.nome,
            fk_disciplina_especialidade = data.fk_disciplina_especialidade
        )
        self.execute_db_query(stmt, False)

    def update(self, data: ProfessorDTO, id: int) -> None:
        stmt = update(
            Professor
        ).where(
            Professor.id == id
        ).values(
            nome = data.nome,
            fk_disciplina_especialidade = data.fk_disciplina_especialidade
        )
        self.execute_db_query(stmt, False)

    def deleted(self, id: int) -> None:
        stmt = delete(
            Professor
        ).where(
            Professor.id == id
        )
        self.execute_db_query(stmt, False)

    def select(selg) -> list:
        stmt = select(
            Professor.id,
            Professor.nome,
            
        )