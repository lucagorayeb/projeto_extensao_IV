from app.backend.services.formato_service import FormatoService as fs


class FormatoController:

    @staticmethod
    def select_formato_controller():
        fs.select_formato_service()

    @staticmethod
    def insert_formato_controller():
        fs.get_from_formatos_service()
