from backend.modules.professor.professor_repository import ProfessorRepository
from backend.modules.professor.professor_dto import ProfessorDTO

class ProfessorService:

    def __init__(self):
        self.repo = ProfessorRepository()

    # def select_professor_service()

    # def select_by_id_professor_service()

    def insrt_professor_service(self, data: ProfessorDTO) -> None:
        self.repo.insert(data)

    def updt_professor_service(self, data: ProfessorDTO, id: int) -> None:
        self.repo.update(data, id)

    def del_professor_service(self, id: int) -> None:
        self.repo.delete(id)

    # def __data_treatment(data: list) -> list:
    #     normalized_data = []
    #     for d in data:
    #         normalized_data.append({
    #             "id": d.
    #         })