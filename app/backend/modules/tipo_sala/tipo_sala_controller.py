from .tipo_sala_service import TipoSalaService


class TipoSalaController:

    def __init__(self):
        self.ctrl = TipoSalaService()

    def slct_tipo_sala_controller(self) -> list[dict]:
        try:
            return self.ctrl.slct_tipo_sala_service()
        except Exception as e:
            print(f"Error: {e}")
            print(f"Error Type: {type(e)}")


    def insrt_tipo_sala_controller(self, data: dict) -> None:
        try:
            self.ctrl.insrt_tipo_sala_service(data=data)
        except Exception as e:
            print(f"Error: {e}")
            print(f"Error Type: {type(e)}")

    def updt_tipo_sala_controller(self, data: dict, id: int) -> None:
        try:
            self.ctrl.updt_tipo_sala_service(data=data, id=id)
        except Exception as e:
            print(f"Error: {e}")
            print(f"Error Type: {type(e)}")

    def del_tipo_sala_controller(self, id: int) -> None:
        try:
            self.ctrl.del_tipo_sala_service(id)
        except Exception as e:
            print(f"Error: {e}")
            print(f"Error Type: {type(e)}")

    def slct_tipo_sala_controller(self, id: int) -> list[dict] | None:
        try:
            return self.ctrl.slct_by_id_tipo_sala_service(id)
        except Exception as e:
            print(f"Error: {e}")
            print(f"Error Type: {type(e)}")
