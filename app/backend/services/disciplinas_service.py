from app.backend.repository.disciplinas_repository import (
    DisciplinaRepository as dr
)


class DisciplinasService:

    @staticmethod
    def select_disciplinas_service():
        dr.select()

    @staticmethod
    def insert_disciplinas_service():
        dr.insert()

    @staticmethod
    def update_disciplinas_service():
        dr.update()

    @staticmethod
    def delete_disciplinas_service():
        dr.delete()
