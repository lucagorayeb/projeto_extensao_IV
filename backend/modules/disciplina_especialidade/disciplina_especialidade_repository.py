from backend.modules.base_repository import BaseRepository
from sqlalchemy import select, insert, update, delete
from backend.modules.disciplina_especialidade.disciplina_especialidade_model import DisciplinaEspecialidade
from backend.modules.disciplina.disciplina_model import Disciplina
from backend.modules.especialidade.especialidade_model import Especialidade
from backend.modules.disciplina_especialidade.disciplina_especialidade_dto import DisciplinaEspecialidadeDTO

class DisciplinaEspecialidadeRepository(BaseRepository):

    def insert(self, data: DisciplinaEspecialidadeDTO) -> None:
        stmt = insert(
            DisciplinaEspecialidade
        ).values(
            fk_disciplina=data.fk_disciplina,
            fk_especialidade=data.fk_especialidade
        )
        self.execute_db_query(stmt, False)

    def delete(self, id: int) -> None:
        stmt = delete(
            DisciplinaEspecialidade
        ).where(
            DisciplinaEspecialidade.id == id
        )
        self.execute_db_query(stmt, False)

    def update(self, data: DisciplinaEspecialidadeDTO, id: int) -> None:
        pass

    def select(self) -> list:
        stmt = select(
            DisciplinaEspecialidade.id,
            Disciplina.id.label('id_disciplina'),
            Disciplina.nome.label('disciplina'),
            Especialidade.id.label('id_especialidade'),
            Especialidade.nome.label('especialidade')
        ).select_from(
            DisciplinaEspecialidade
        ).join(
            Disciplina, DisciplinaEspecialidade.fk_disciplina == Disciplina.id
        ).join(
            Especialidade, DisciplinaEspecialidade.fk_especialidade == Especialidade.id
        )
        return self.execute_db_query(stmt, True)

    def select_by_id(self, id: int) -> list:
        stmt = select(
            DisciplinaEspecialidade.id,
            Disciplina.id.label('id_disciplina'),
            Disciplina.nome.label('disciplina'),
            Especialidade.id.label('id_especialidade'),
            Especialidade.nome.label('especialidade')
        ).select_from(
            DisciplinaEspecialidade
        ).join(
            Disciplina, DisciplinaEspecialidade.fk_disciplina == Disciplina.id
        ).join(
            Especialidade, DisciplinaEspecialidade.fk_especialidade == Especialidade.id
        ).where(
            DisciplinaEspecialidade.id == id
        )
        return self.execute_db_query(stmt, True)
