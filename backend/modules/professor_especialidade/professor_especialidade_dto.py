from pydantic import BaseModel

class ProfessorEspecialidadeDTO(BaseModel):
    fk_professor: int
    fk_especialidade: int