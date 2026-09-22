from disciplinas_service import (
    DisciplinasService as ds
)


class DisciplinasController:

    @staticmethod
    def select_disciplinas_controller():
        ds.select_disciplinas_service()

    @staticmethod
    def insert_disciplinas_controller():
        ds.insert_disciplinas_service()

    @staticmethod
    def update_disciplinas_controller():
        ds.update_disciplinas_service()

    @staticmethod
    def delete_disciplinas_controller():
        ds.delete_disciplinas_service()
