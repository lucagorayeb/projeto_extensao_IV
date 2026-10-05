from .formato_repository import FormatoRepository


class FormatoService:

    def __init__(self):
        self.repo = FormatoRepository()

    def slct_formato_service(self) -> list[dict] | None:
        return self.repo.select()

    def insrt_formato_service(self, data: dict) -> None:
        self.repo.insert(data)

    def updt_formato_service(self, data: dict, id: int) -> None:
        data["id"] = id
        self.repo.update(data)

    def del_formato_service(self, id: int) -> None:
        data = {"id": id}
        self.repo.delete(data)

    def slct_by_id_formato_service(self, id: int) -> list[dict] | None:
        data = {"id": id}
        return self.repo.select_by_id(data=data)
