from backend.modules.base_repository import BaseRepository
from sqlalchemy import insert, update, delete, select
from backend.modules.turma.turma_model import Turma
from backend.modules.professor.professor_model import Professor
from backend.modules.disciplina.disciplina_model import Disciplina
from backend.modules.sala.sala_model import Sala
from backend.modules.dia_semana.dia_semana import dia_semana


class TurmaRepository(BaseRepository):

    def insert(self, data: dict) -> None:
        stmt = insert(
            Turma
        ).values(
            fk_disciplina = data['fk_disciplina'],
            fk_sala = data['fk_sala'],
            fk_professor = data['fk_professor'],
            fk_dia_semana = data['fk_dia_semana'],
            horario_inicio = data['horario_inicio'],
            horario_fim = data['horario_fim']
        )
        self.execute_db_query(stmt, False)

    def update(self, data: dict) -> None:
        stmt = update(
            Turma
        ).where(
            Turma.id == data['id']
        ).values(
            fk_disciplina = data['fk_disciplina'],
            fk_sala = data['fk_sala'],
            fk_professor = data['fk_professor'],
            fk_dia_semana = data['fk_dia_semana'],
            horario_inicio = data['horario_inicio'],
            horario_fim = data['horario_fim']
        )
        self.execute_db_query(stmt, False)

    def delete(self, id: int) -> None:
        stmt = delete(
            Turma
        ).where(
            Turma.id == id
        )
        self.execute_db_query(stmt, False)

    def select(self) -> list:
        stmt = select(
            Turma.id,
            Disciplina.id.label('fk_disciplina'),
            Disciplina.nome.label('fk_disciplina_nome'),
            Sala.id.label('fk_sala'),
            Sala.nome.label('fk_sala_nome'),
            Professor.id.label('fk_professor'),
            Professor.nome.label('fk_professor_nome'),
            dia_semana.c.id.label('fk_dia_semana'),
            dia_semana.c.nome.label('fk_dia_semana_nome'),
            Disciplina.carga_horaria,
            Turma.horario_inicio,
            Turma.horario_fim
        ).join(
            Disciplina, Disciplina.id == Turma.fk_disciplina
        ).join(
            Sala, Sala.id == Turma.fk_sala
        ).join(
            Professor, Professor.id == Turma.fk_professor
        ).join(
            dia_semana, dia_semana.c.id == Turma.fk_dia_semana
        )
        return self.execute_db_query(stmt, True)

    def get_dias_semana(self) -> list:
        stmt = select(
            dia_semana.c.id,
            dia_semana.c.nome
        )
        return self.execute_db_query(stmt, True)