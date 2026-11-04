from pydantic import BaseModel

class ProfessorDTO(BaseModel):
    
    nome: str
    fk_disciplina_especialidade: int