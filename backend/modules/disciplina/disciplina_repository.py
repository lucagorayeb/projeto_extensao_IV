from sqlalchemy import select, update, delete, insert
from backend.modules.base_repository import BaseRepository
from backend.modules.disciplina.disciplina_model import Disciplina
from backend.modules.formato.formato_model import Formato
from backend.modules.disciplina.disciplina_dto import DisciplinaDTO


class DisciplinaRepository(BaseRepository):

    def insert(self, data: DisciplinaDTO) -> None:
        stmt = insert(
            Disciplina
        ).values(
            nome=data.nome,
            fk_formato=data.fk_formato,
            carga_horaria=data.carga_horaria,
            pratica=data.pratica
        )
        self.execute_db_query(stmt, False)

    def select(self) -> list:
        stmt = select(
            Disciplina.id,
            Disciplina.nome,
            Disciplina.carga_horaria,
            Disciplina.pratica,
            Disciplina.fk_formato.label('formato_id'),
            Formato.nome.label('formato')
        ).select_from(
            Formato
        ).join(
            Disciplina, Formato.id == Disciplina.fk_formato
        ).order_by(
            Disciplina.id
        )
        return self.execute_db_query(stmt, True).all()

    def update(self, data: DisciplinaDTO, id: int) -> None:
        stmt = update(
            Disciplina
        ).where(
            Disciplina.id == id
        ).values(
            nome=data.nome,
            fk_formato=data.fk_formato,
            carga_horaria=data.carga_horaria,
            pratica=data.pratica
        )
        self.execute_db_query(stmt, False)

    def delete(self, id: int) -> None:
        stmt = delete(
            Disciplina
        ).where(
            Disciplina.id == id
        )
        self.execute_db_query(stmt, False)

    def select_by_id(self, id: int) -> list:
        stmt = select(
            Disciplina.id,
            Disciplina.nome,
            Disciplina.carga_horaria,
            Disciplina.pratica,
            Disciplina.fk_formato.label('formato_id'),
            Formato.nome.label('formato')
        ).select_from(
            Formato
        ).join(
            Disciplina, Formato.id == Disciplina.fk_formato
        ).order_by(
            Disciplina.id
        ).where(
            Disciplina.id == id
        )
        return self.execute_db_query(stmt, True).all()