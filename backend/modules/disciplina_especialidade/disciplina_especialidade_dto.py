from pydantic import BaseModel

class DisciplinaEspecialidadeDTO(BaseModel):
    fk_disciplina: int
    fk_especialidade: int