from .formato_service import FormatoService


class FormatoController:

    def __init__(self):
        self.serv = FormatoService()

    def slct_formato_controller(self) -> list[dict] | None:
        return self.serv.slct_formato_service()

    def insrt_formato_controller(self, data: dict) -> None:
        self.serv.insrt_formato_service(data)

    def updt_formato_controller(self, data: dict, id: int) -> None:
        self.serv.updt_formato_service(data, id)

    def del_formato_controller(self, id: int) -> None:
        self.serv.del_formato_service(id)

    def slct_by_id_formato_controller(self, id: int) -> list[dict] | None:
        return self.serv.slct_by_id_formato_service(id)
