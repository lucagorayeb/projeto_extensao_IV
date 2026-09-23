from disciplinas_service import (
    DisciplinasService as serv
)


class DisciplinasController:

    @staticmethod
    def select_disciplinas_controller():
        serv.select_disciplinas_service()

    @staticmethod
    def insert_disciplinas_controller():
        serv.insert_disciplinas_service()

    @staticmethod
    def update_disciplinas_controller():
        serv.update_disciplinas_service()

    @staticmethod
    def delete_disciplinas_controller():
        serv.delete_disciplinas_service()
