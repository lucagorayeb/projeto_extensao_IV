from formatos_repository import (
    FormatoRepository as repo
)


class FormatoService:

    @staticmethod
    def select_formato_service():
        repo.select()

    @staticmethod
    def insert_formato_service():
        repo.insert()

    @staticmethod
    def update_formato_service():
        repo.update()

    @staticmethod
    def delete_formato_service():
        repo.delete()
