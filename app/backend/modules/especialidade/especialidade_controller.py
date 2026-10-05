from .especialidade_service import EspecialidadeService


class EspecialidadeController:

    def __init__(self):
        self.serv = EspecialidadeService()

    def slct_especialidade_controller(self) -> list[dict] | None:
        return self.serv.slct_especialidade_service()

    def insrt_especialidade_controller(self, data: dict) -> None:
        self.serv.insrt_especialidade_service(data=data)

    def updt_especialidade_controller(self, data: dict, id: int) -> None:
        self.serv.updt_especialidade_service(data=data, id=id)

    def del_especialidade_controller(self, id: int) -> None:
        self.serv.del_especialidade_service(id=id)

    def slct_by_id_especialidade_controller(self, id: int) -> list[dict] | None:
        return self.serv.slct_especialidade_service(id)
