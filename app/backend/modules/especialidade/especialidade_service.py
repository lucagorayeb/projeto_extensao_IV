from .especialidade_repository import EspecialidadeRepository


class EspecialidadeService:

    def __init__(self):
        self.repo = EspecialidadeRepository()

    def slct_especialidade_service(self) -> list[dict] | None:
        return self.repo.select()

    def insrt_especialidade_service(self, data: dict) -> None:
        self.repo.insert(data)

    def updt_especialidade_service(self, data: dict, id: int) -> None:
        data["id"] = id
        self.repo.update(data=data)

    def del_especialidade_service(self, id: int) -> None:
        data = {"id": id}
        self.repo.delete(data=data)

    def slct_by_id_especialidade_service(self, id: int) -> list[dict] | None:
        data = {"id": id}
        return self.repo.select_by_id(data=data)
