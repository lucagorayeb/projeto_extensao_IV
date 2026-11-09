from backend.modules.base_repository import BaseRepository
from sqlalchemy import insert, update, delete, select
from backend.modules.professor.professor_model import Professor
from backend.modules.professor.professor_dto import ProfessorDTO

class ProfessorRepository(BaseRepository):

    def insert(self, data: ProfessorDTO) -> None:
        stmt = insert(
            Professor
        ).values(
            nome = data['nome'],
            cpf = data['cpf']
        )
        self.execute_db_query(stmt, False)

    def update(self, data: ProfessorDTO, id: int) -> None:
        stmt = update(
            Professor
        ).where(
            Professor.id == id
        ).values(
            nome = data['nome'],
            cpf = data['cpf']
        )
        self.execute_db_query(stmt, False)

    def delete(self, id: int) -> None:
        stmt = delete(
            Professor
        ).where(
            Professor.id == id
        )
        self.execute_db_query(stmt, False)

    def select(selg) -> list:
        # stmt = select(
        #     Professor.id,
        #     Professor.nome,
            
        # )
        pass