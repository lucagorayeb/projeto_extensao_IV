from backend.modules.base_model.model import DefaultModel, initpk, timestamp
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from datetime import time
from sqlalchemy import Time

class Turma(DefaultModel):
    __tablename__ = 'turma'

    id: Mapped[initpk]
    fk_disciplina: Mapped[int] = mapped_column(ForeignKey("disciplina.id"))
    fk_sala: Mapped[int] = mapped_column(ForeignKey("sala.id"))
    fk_professor: Mapped[int] = mapped_column(ForeignKey('professor.id'))
    fk_dia_semana: Mapped[int] = mapped_column(ForeignKey('dia_semana.id'))
    carga_horaria: Mapped[time] = mapped_column(Time, nullable=False)
    horario_inicio: Mapped[time] = mapped_column(Time, nullable=False)
    horario_fim: Mapped[time] = mapped_column(Time, nullable=False)
    created_at: Mapped[timestamp]
    updated_at: Mapped[timestamp]