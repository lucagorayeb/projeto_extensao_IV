from .formatos_service import FormatoService as serv


class FormatoController:

    
    def slct_formato_controller(self) -> list[tuple]:
        return serv.select_formato_service()

    
    def insrt_formato_controller(self, data: list[tuple]):
        serv.insert_formato_service(data)

    
    def update_formato_controller(self, data: list[tuple], id: int):
        serv.update_formato_service(data, id)

    
    def delete_formato_controller(self, id: int):
        serv.delete_formato_service(id)
