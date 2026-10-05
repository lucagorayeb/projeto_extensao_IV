from .tipo_sala_repository import TipoSalaRepository


class TipoSalaService:

    def __init__(self):
        self.serv = TipoSalaRepository()

    def slct_tipo_sala_service(self) -> list[dict]:
        return self.serv.select()

    def insrt_tipo_sala_service(self, data: dict) -> None:
        self.serv.insert(data=data)

    def updt_tipo_sala_service(self, data: dict, id: int) -> None:
        data['id'] = id
        self.serv.update(data=data)

    def del_tipo_sala_service(self, id: int) -> None:
        data = {'id': id}
        self.serv.delete(data=data)

    def slct_by_id_tipo_sala_service(self, id: int) -> list[dict] | None:
        data = {'id': id}
        self.serv.select_by_id(data=data)
