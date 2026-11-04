from backend.modules.base_model.model import DefaultModel, initpk, timestamp
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import  ForeignKey

class DisciplinaEspecialidade(DefaultModel):

    __tablename__ = "disciplina_especialidade"

    id: Mapped[initpk]
    fk_disciplina: Mapped[int] = mapped_column(ForeignKey("disciplina.id"))
    fk_especialidade: Mapped[int] = mapped_column(ForeignKey("especialidade.id"))
    created_at: Mapped[timestamp]
    updated_at: Mapped[timestamp]