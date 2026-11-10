from backend.modules.base_repository import BaseRepository
from sqlalchemy import insert, update, delete, select, text
from backend.modules.professor.professor_model import Professor
from backend.modules.professor.professor_dto import ProfessorDTO
from backend.modules.especialidade.especialidade_model import Especialidade
from backend.modules.professor_especialidade.professor_especialidade_model import ProfessorEspecialidade

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

    def select(self) -> list:
        stmt = select(
            Professor.id.label('professor_id'),
            Professor.nome.label('professor_nome'),
            Professor.cpf.label('professor_cpf'),
            Especialidade.id.label('especialidade_id'),
            Especialidade.nome.label('especialidade_nome')
        ).join(
            ProfessorEspecialidade, ProfessorEspecialidade.fk_professor == Professor.id, isouter=True
        ).join(
            Especialidade,  ProfessorEspecialidade.fk_especialidade == Especialidade.id, isouter=True
        )
        return self.execute_db_query(stmt, True)