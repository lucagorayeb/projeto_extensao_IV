from backend.modules.disciplina_especialidade.disciplina_especialidade_repository import DisciplinaEspecialidadeRepository
from backend.modules.disciplina_especialidade.disciplina_especialidade_dto import DisciplinaEspecialidadeDTO

class DisciplinaEspecialidadeService:

    def __init__(self):
        self.repo = DisciplinaEspecialidadeRepository()

    def insrt_disciplina_especialidade_service(self, data: DisciplinaEspecialidadeDTO) -> None:
        self.repo.insert(data)

    def del_disciplina_especialidade_service(self, id: int) -> None:
        self.repo.delete(id)

    def slct_disciplina_especialidade_service(self) -> list:
        data = self.repo.select()
        return self.__data_treatment(data)

    def slct_by_id_disciplina_especialidade_service(self, id: int) -> list:
            data = self.repo.select_by_id(id)
            return self.__data_treatment(data)

    def __data_treatment(self, data: list) -> list:
        normalized_data = []
        print(data)
        for d in data:
            normalized_data.append({
                "id": d.id,
                "id_disciplina": d.id_disciplina,
                "disciplina": d.disciplina,
                "id_especialidade": d.id_especialidade,
                "especialidade": d.especialidade
            })
        return normalized_data