from disciplinas_service import (
    DisciplinasService as serv
)


class DisciplinasController:

    def slct_disciplinas_controller(self) -> list[tuple]:
        return serv.slct_disciplinas_service()

    def insrt_disciplinas_controller(self, data: list[tuple]) -> None:
        serv.insrt_disciplinas_service(data)

    def updt_disciplinas_controller(self, data: list[tuple], id: int) -> None:
        serv.updt_disciplinas_service(data, id)

    def del_disciplinas_controller(self, id: int) -> None:
        serv.del_disciplinas_service()
