from backend.modules.disciplina.disciplina_service import DisciplinaService
from backend.modules.disciplina.disciplina_dto import DisciplinaDTO
from sqlalchemy.exc import IntegrityError, NoResultFound, SQLAlchemyError
from http import HTTPStatus

class DisciplinaController:

    def __init__(self):
        self.serv = DisciplinaService()

    def slct_disciplina_controller(self) -> dict:
        try:
            data = self.serv.slct_disciplina_service()
        except (IntegrityError, NoResultFound):
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
                "content": "Internal Error"
            }
        return {
            "status_code": HTTPStatus.OK,
            "content": data
        }

    def insrt_disciplina_controller(self, data: DisciplinaDTO) -> dict:
        try:
            self.serv.insrt_disciplina_service(data)
        except (IntegrityError, NoResultFound):
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
                "content": "Internal Error"
            }
        return {
            "status_code": HTTPStatus.CREATED,
            "content": "Disciplina Object Created"
        }

    def updt_disciplina_controller(self, data: DisciplinaDTO, id: int) -> dict:
        try:
            self.serv.updt_disciplina_service(data, id)
        except (IntegrityError, NoResultFound):
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
                "content": "Internal Error"
            }
        return {
            "status_code": HTTPStatus.OK,
            "content": "Disciplina Objected Updated"
        }

    def del_disciplina_controller(self, id: int) -> dict:
        try:
            self.serv.del_disciplina_service(id)
        except (IntegrityError, NoResultFound):
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
                "content": "Internal Error"
            }
        return {
            "status_code": HTTPStatus.OK,
            "content": "Disciplina Objected Deleted"
        }

    def slct_by_id_disciplina_controller(self, id: int) -> dict:
        try:
            data = self.serv.slct_by_id_disciplina_service(id)
        except (IntegrityError, NoResultFound):
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
                "content": "Internal Error"
            }
        return {
            "status_code": HTTPStatus.OK,
            "content": data
        }