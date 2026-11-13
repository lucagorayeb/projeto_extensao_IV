from backend.modules.base_model.model import DefaultModel, initpk, str_50, num_5_2, timestamp
from sqlalchemy.orm import Mapped

class Disciplina(DefaultModel):

    __tablename__ = "disciplina"

    id: Mapped[initpk]
    nome: Mapped[str_50]
    fk_formato: Mapped[int]
    carga_horaria: Mapped[num_5_2]
    pratica: Mapped[int]
    created_at: Mapped[timestamp]
    updated_at: Mapped[timestamp]
