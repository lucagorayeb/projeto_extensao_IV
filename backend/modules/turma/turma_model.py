from backend.modules.base_model.model import DefaultModel, initpk, timestamp
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Time, UniqueConstraint
from datetime import time

class Turma(DefaultModel):
    __tablename__ = 'turma'

    __table_args__ = (
        UniqueConstraint(
            "fk_sala", "fk_dia_semana",
            name="uq_turma_sala_dia",
        ),
    )

    id: Mapped[initpk]
    fk_disciplina: Mapped[int] = mapped_column(ForeignKey("disciplina.id"))
    fk_sala: Mapped[int] = mapped_column(ForeignKey("sala.id"))
    fk_professor: Mapped[int] = mapped_column(ForeignKey('professor.id'))
    fk_dia_semana: Mapped[int] = mapped_column(ForeignKey('dia_semana.id'))
    horario_inicio: Mapped[time] = mapped_column(Time, nullable=False)
    horario_fim: Mapped[time] = mapped_column(Time, nullable=False)
    created_at: Mapped[timestamp]
    updated_at: Mapped[timestamp]
