from ..base_model.model import DefaultModel, str_30, initpk, timestamp
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class Professor(DefaultModel):

    __tablename__ = "professor"

    id: Mapped[initpk]
    nome: Mapped[str_30]
    fk_disciplina_especialidade: Mapped[int] = mapped_column(ForeignKey("disciplina_especialidade.id"))
    created_at: Mapped[timestamp]
    updated_at: Mapped[timestamp]