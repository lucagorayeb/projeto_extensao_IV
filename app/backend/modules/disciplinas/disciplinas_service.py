from disciplinas_repository import (
    DisciplinaRepository as repo
)


class DisciplinasService:

    def slct_disciplinas_service(self, data: list[tuple]) -> list[tuple]:
        return repo.select(data)

    def insrt_disciplinas_service(self, data: list[tuple]) -> None:
        repo.insert(data)

    def updt_disciplinas_service(self, data: list[tuple], id: int) -> None:
        repo.update(data, id)

    def del_disciplinas_service(self, id: int) -> None:
        repo.delete(id)
