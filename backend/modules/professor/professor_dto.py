from pydantic import BaseModel

class ProfessorDTO(BaseModel):
    
    nome: str
    cpf: str