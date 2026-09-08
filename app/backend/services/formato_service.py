from app.backend.repository.formato_repository import (
    FormatoRepository as fr
)


class FormatoService:

    @staticmethod
    def select_formato_service():
        fr.select()

    @staticmethod
    def insert_formato_service():
        fr.insert()

    @staticmethod
    def update_formato_service():
        fr.update()

    @staticmethod
    def delete_formato_service():
        fr.delete()
