from backend.modules.base_model.model import DefaultModel, initpk, timestamp
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class ProfessorEspecialidade(DefaultModel):

    __tablename__ = "professor_especialidade"

    id: Mapped[initpk]
    fk_professor: Mapped[int] = mapped_column(ForeignKey("professor.id"))
    fk_especialidade: Mapped[int] = mapped_column(ForeignKey("especialidade.id"))
    created_at: Mapped[timestamp]
    updated_at: Mapped[timestamp]