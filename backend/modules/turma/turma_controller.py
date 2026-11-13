from backend.modules.turma.turma_service import TurmaService
from backend.modules.turma.turma_dto import TurmaDTO


class TurmaController:

    def __init__(self):
        self.serv = TurmaService()

    def insrt_turma_controller(self, data: dict) -> None:
        self.serv.insrt_turma_service(data)

    def updt_turma_controller(self, data: dict, id: int) -> None:
        self.serv.updt_turma_service(data, id)

    def del_turma_controller(self, id: int) -> None:
        self.serv.del_turma_service(id)

    def slct_turma_controller(self) -> list:
        return self.serv.slct_turma_service()

    def get_dias_semana_controller(self) -> list:
        return self.serv.get_dias_semana_service()
