from .sala_service import SalaService
from ..base_json.return_json import ReturnJson


class SalaController:

    def __init__(self):    
        self.ctrl = SalaService()
        self.json = ReturnJson()

    def insrt_sala_controller(self, data: dict):
        try:
            self.ctrl.insrt_sala_service(data=data)
        except Exception as e:
            # print(e)
            array_erro = []
            # erro = 
            print(e.)
            array_erro.append({
                "error": str(e),
                "error_type": str(type(e)),
                "status": 400,
                "description": "Bad Request"
            })
            # print(array_erro)
            # return erro
            # teste = self.json.return_format_data(array_erro)
            # print(teste)
            # return teste

    def updt_sala_controller(self, data: dict, id: int) -> None:
        self.ctrl.updt_sala_service(data=data, id=id)

    def del_sala_controller(self, id: int) -> None:
        self.ctrl.del_sala_service(id=id)

    def slct_sala_controller(self) -> str:
        return self.ctrl.slct_sala_service()

    def slct_by_id_sala_controller(self, id: int) -> str:
        return self.ctrl.slct_by_id_sala_service(id=id)
