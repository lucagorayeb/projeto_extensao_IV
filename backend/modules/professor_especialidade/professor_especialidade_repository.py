from backend.modules.base_repository import BaseRepository
from sqlalchemy import insert, update, delete, select
from backend.modules.professor_especialidade.professor_especialidade_model import ProfessorEspecialidade
from backend.modules.professor.professor_model import Professor
from backend.modules.especialidade.especialidade_model import Especialidade


class ProfessorEspecialidadeRepository(BaseRepository): 
    
    def select(self) -> list:
        stmt = select(
            Especialidade.id,
            Especialidade.nome
        ).join(
            ProfessorEspecialidade, ProfessorEspecialidade.fk_especialidade == Especialidade.id
        ).join(
            Professor,  ProfessorEspecialidade.fk_professor == Professor.id
        )
        return self.execute_db_query(stmt, True)

    def insert(self, data: dict) -> None:
        stmt = insert(
                ProfessorEspecialidade
            ).values(
                fk_professor=data['fk_professor'],
                fk_especialidade=data['fk_especialidade']
            )
        self.execute_db_query(stmt, False)
    
    def update(data: dict, id: int) -> None:
        pass
    
    def delete(self, id: int) -> None:
        stmt = delete(
            ProfessorEspecialidade
        ).where(
            ProfessorEspecialidade.id == id
        )
        self.execute_db_query(stmt, False)

    def select_by_id(self, id: int) -> list:
        stmt = select(
            Especialidade.id,
            Especialidade.nome
        ).join(
            ProfessorEspecialidade, ProfessorEspecialidade.fk_especialidade == Especialidade.id
        ).join(
            Professor,  ProfessorEspecialidade.fk_professor == Professor.id
        ).where(
            ProfessorEspecialidade.fk_professor == id
        )
        return self.execute_db_query(stmt, True)

    def slct_especialidades_professor(self, id: int) -> list:
        stmt = select(
            ProfessorEspecialidade.fk_especialidade,
        ).where(
            ProfessorEspecialidade.fk_professor == id
        )
        return self.execute_db_query(stmt, True)
