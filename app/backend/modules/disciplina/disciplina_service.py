from .disciplina_repository import DisciplinaRepository
from .disciplina_dto import DisciplinaDTO


class DisciplinaService:

    def __init__(self):
        self.repo = DisciplinaRepository()

    def slct_disciplina_service(self):
        data = self.repo.select()
        return self.__data_treatment(data)

    def insrt_disciplina_service(self, data: DisciplinaDTO) -> None:
        self.repo.insert(data)

    def updt_disciplina_service(self, data: DisciplinaDTO, id: int) -> None:
        self.repo.update(data, id)

    def del_disciplina_service(self, id: int) -> None:
        self.repo.delete(id)

    def slct_by_id_disciplina_service(self, id: int) -> list:
        data = self.repo.select_by_id(id)
        return self.__data_treatment(data)

    def __data_treatment(self, data: DisciplinaDTO) -> list:
        normalized_data = []
        for d in data:
            normalized_data.append({
                "id": d.id,
                "nome": d.nome,
                "formato_id": d.formato_id,
                "formato": d.formato,
                "carga_horaria": float(d.carga_horaria),
                "horario_inicio": str(d.horario_inicio),
                "horario_termino": str(d.horario_termino),
                "pratica": d.pratica
            })
        return normalized_data