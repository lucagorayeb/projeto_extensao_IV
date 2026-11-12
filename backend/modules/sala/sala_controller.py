from backend.modules.sala.sala_service import SalaService
from backend.modules.sala.sala_dto import SalaDTO
from sqlalchemy.exc import IntegrityError, NoResultFound, SQLAlchemyError
from http import HTTPStatus

class SalaController:

    def __init__(self):    
        self.ctrl = SalaService()

    def insrt_sala_controller(self, data: SalaDTO) -> dict:
        try:
            self.ctrl.insrt_sala_service(data)
        except (IntegrityError, NoResultFound):
            return {
                "status_code":HTTPStatus.BAD_REQUEST,
                "content":"Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code":HTTPStatus.INTERNAL_SERVER_ERROR,
                "content":"Internal Error"
            }
        return {
            "status_code": HTTPStatus.CREATED,
            "content": "Sala Object Created"
        }

    def updt_sala_controller(self, data: SalaDTO, id: int) -> dict:
        try:
            self.ctrl.updt_sala_service(data, id)
        except (IntegrityError, NoResultFound):
            return {
                "status_code":HTTPStatus.BAD_REQUEST,
                "content":"Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code":HTTPStatus.INTERNAL_SERVER_ERROR,
                "content":"Internal Error"
            }
        return {
            "status_code":HTTPStatus.OK,
            "content":"Sala Objected Updated"
        }

    def del_sala_controller(self, data: dict) -> dict:
        try:
            self.ctrl.del_sala_service(data)
        except (IntegrityError, NoResultFound):
            return {
                "status_code":HTTPStatus.BAD_REQUEST,
                "content":"Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code":HTTPStatus.INTERNAL_SERVER_ERROR,
                "content":"Internal Error"
            }
        return {
            "status_code": HTTPStatus.OK,
            "content": "Sala Objected Deleted"
        }

    def slct_sala_controller(self) -> dict:
        try:
            data = self.ctrl.slct_sala_service()
        except (IntegrityError, NoResultFound):
            return {
                "status_code":HTTPStatus.BAD_REQUEST,
                "content":"Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code":HTTPStatus.INTERNAL_SERVER_ERROR,
                "content":"Internal Error"
            }
        return {
            "status_code": HTTPStatus.OK,
            "content": data
        }

    def slct_by_id_sala_controller(self, data: dict) -> dict:
        try:
            data = self.ctrl.slct_by_id_sala_service(data)
        except (IntegrityError, NoResultFound):
            return {
                "status_code":HTTPStatus.BAD_REQUEST,
                "content":"Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code":HTTPStatus.INTERNAL_SERVER_ERROR,
                "content":"Internal Error"
            }
        return {
            "status_code":HTTPStatus.OK,
            "content":data
        }
