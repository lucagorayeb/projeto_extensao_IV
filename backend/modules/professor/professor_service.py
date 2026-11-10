from backend.modules.professor.professor_repository import ProfessorRepository
from backend.modules.professor.professor_dto import ProfessorDTO

class ProfessorService:

    def __init__(self):
        self.repo = ProfessorRepository()

    def slct_professor_service(self) -> list:
        data = self.repo.select()
        return self.__data_treatment(data)

    # def select_by_id_professor_service()

    def insrt_professor_service(self, data: ProfessorDTO) -> None:
        self.repo.insert(data)

    def updt_professor_service(self, data: ProfessorDTO, id: int) -> None:
        self.repo.update(data, id)

    def del_professor_service(self, id: int) -> None:
        self.repo.delete(id)

    def __data_treatment(self, data: ProfessorDTO) -> list:
        normalized_data = []
        for d in data:
            normalized_data.append({
                "id": d.professor_id,
                "nome": d.professor_nome,
                "cpf": d.professor_cpf,
                "especialidade_id": d.especialidade_id,
                "especialidade": d.especialidade_nome
            })
        return normalized_data