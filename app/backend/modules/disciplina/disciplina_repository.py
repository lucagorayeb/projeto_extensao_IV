from sqlalchemy import select, update, delete, insert
from ..base_repository import BaseRepository
from .disciplina_model import Disciplina
from ..formato.formato_model import Formato
from .disciplina_dto import DisciplinaDTO


class DisciplinaRepository(BaseRepository):

    def insert(self, data: DisciplinaDTO) -> None:
        stmt = insert(
            Disciplina
        ).values(
            nome=data.nome,
            fk_formato=data.fk_formato,
            carga_horaria=data.carga_horaria,
            horario_inicio=data.horario_inicio,
            horario_termino=data.horario_termino,
            pratica=data.pratica
        )
        self.execute_db_query(stmt, False)

    def select(self) -> list:
        stmt = select(
            Disciplina.id,
            Disciplina.nome,
            Disciplina.carga_horaria,
            Disciplina.horario_inicio,
            Disciplina.horario_termino,
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
            horario_inicio=data.horario_inicio,
            horario_termino=data.horario_termino,
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
            Disciplina.horario_inicio,
            Disciplina.horario_termino,
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