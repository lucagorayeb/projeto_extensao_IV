from backend.modules.professor_especialidade.professor_especialidade_dto import ProfessorEspecialidadeDTO
from backend.modules.professor_especialidade.professor_especialidade_repository import ProfessorEspecialidadeRepository


class ProfessorEspecialidadeService:

    def __init__(self):
        self.repo = ProfessorEspecialidadeRepository()

    def insrt_professor_especialidade_service(self, data: dict) -> None:
        especialidades_existentes = self.__retorna_as_especialidades_do_professor(data['fk_professor'])
        if int(data['fk_especialidade']) not in especialidades_existentes: 
            self.repo.insert(data)  

    def del_professor_especialidade_service(self, data: dict) -> None:
        id = int(data['id'])
        self.repo.delete(id)

    def slct_professor_especialidade_service(self) -> list:
        data = self.repo.select()
        return self.__data_treatment(data)

    def slct_by_id_professor_especialidade_service(self, id: int) -> list:
        # id = int(data['id'])
        data = self.repo.select_by_id(id)
        return self.__data_treatment(data)

    def __data_treatment(self, data: list) -> list:
        normalized_data = []
        for d in data:
            normalized_data.append({
                "id": d.id,
                "nome": d.nome
            })
        return normalized_data

    def __retorna_as_especialidades_do_professor(self, id: int) -> list:
        data = self.repo.slct_especialidades_do_professor(id)
        array_especialidades = []
        for d in data:
            array_especialidades.append(d.fk_especialidade)
        return array_especialidades