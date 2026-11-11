from backend.modules.tipo_sala.tipo_sala_service import TipoSalaService
from sqlalchemy.exc import IntegrityError, NoResultFound, SQLAlchemyError
from backend.modules.tipo_sala.tipo_sala_dto import TipoSalaDTO
from fastapi.responses import JSONResponse
from http import HTTPStatus

class TipoSalaController:

    def __init__(self):
        self.ctrl = TipoSalaService()

    def slct_tipo_sala_controller(self) -> dict:
        try:
            data = self.ctrl.slct_tipo_sala_service()
        except IntegrityError:
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except NoResultFound:
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
                "content": "Internal Error"
            }
        except Exception:
            return {
                "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
                "content": "Internal Error"
            }
        return {
            "status_code": HTTPStatus.OK,
            "content": data
        }

    def insrt_tipo_sala_controller(self, data: TipoSalaDTO) -> dict:
        try:
            self.ctrl.insrt_tipo_sala_service(data=data)
        except IntegrityError:
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except NoResultFound:
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
            "content": "Tipo Sala Objected Created"
        }
    
    def updt_tipo_sala_controller(self, data: dict, id: int) -> dict:
        try:
            self.ctrl.updt_tipo_sala_service(data=data, id=id)
        except IntegrityError:
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except NoResultFound:
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code": 500,
                "content": "Internal Error"
            }
        return {
            "status_code": HTTPStatus.OK,
            "content": "Tipo Sala Objected Updated"
        }
    
    def del_tipo_sala_controller(self, id: int) -> JSONResponse:
        try:
            self.ctrl.del_tipo_sala_service(id)
        except IntegrityError:
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except NoResultFound:
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code": 500,
                "content": "Internal Error"
            }
        return {
            "status_code": HTTPStatus.OK,
            "content": "Sala Objected Deleted"
        }
    
    def slct_by_id_tipo_sala_controller(self, id: int) -> JSONResponse:
        try:
            data = self.ctrl.slct_by_id_tipo_sala_service(id)
        except IntegrityError:
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except NoResultFound:
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code": 500,
                "content": "Internal Error"
            }
        except Exception:
            return {
                "status_code": HTTPStatus.NOT_FOUND,
                "content": "Not Found"
            }
        return {
            "status_code": HTTPStatus.OK,
            "content": data
        }