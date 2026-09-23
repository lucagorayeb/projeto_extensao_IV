from disciplinas_repository import (
    DisciplinaRepository as repo
)


class DisciplinasService:

    @staticmethod
    def select_disciplinas_service():
        repo.select()

    @staticmethod
    def insert_disciplinas_service():
        repo.insert()

    @staticmethod
    def update_disciplinas_service():
        repo.update()

    @staticmethod
    def delete_disciplinas_service():
        repo.delete()
