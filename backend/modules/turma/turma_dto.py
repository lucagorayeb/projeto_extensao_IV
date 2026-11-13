from pydantic import BaseModel
from datetime import time

class TurmaDTO(BaseModel):
    fk_disciplina: int
    fk_sala: int
    fk_professor: int
    fk_dia_semana: int
    carga_horaria: time
    horario_inicio: time
    horario_fim: time
