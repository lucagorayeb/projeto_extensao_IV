from formatos_service import FormatoService as serv


class FormatoController:

    @staticmethod
    def select_formato_controller():
        serv.select_formato_service()

    @staticmethod
    def insert_formato_controller():
        serv.insert_formato_service()

    @staticmethod
    def update_formato_controller():
        serv.update_formato_service()

    @staticmethod
    def delete_formato_controller():
        serv.delete_formato_service()
