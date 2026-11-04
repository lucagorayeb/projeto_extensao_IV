from pydantic import BaseModel
from datetime import time

class DisciplinaDTO(BaseModel):
    nome: str
    fk_formato: int
    carga_horaria: float
    horario_inicio: time
    horario_termino: time
    pratica: int