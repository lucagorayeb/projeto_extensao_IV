from backend.modules.professor_especialidade.professor_especialidade_dto import ProfessorEspecialidadeDTO
from backend.modules.professor_especialidade.professor_especialidade_repository import ProfessorEspecialidadeRepository


class ProfessorEspecialidadeService:

    def __init__(self):
        self.repo = ProfessorEspecialidadeRepository()

    def insrt_professor_especialidade_service(self, data: dict) -> None:
        self.repo.insert(data)

    def del_professor_especialidade_service(self, data: dict) -> None:
        id = int(data['id'])
        self.repo.delete(id)

    def slct_professor_especialidade_service(self) -> list:
        data = self.repo.select()
        return self.__data_treatment(data)

    def __data_treatment(self, data: list) -> list:
        normalized_data = []
        for d in data:
            normalized_data.append({
                "id": d.id,
                "nome": d.nome
            })
        return normalized_data