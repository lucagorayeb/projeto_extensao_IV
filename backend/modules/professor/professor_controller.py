from backend.modules.professor.professor_service import ProfessorService
from backend.modules.professor.professor_dto import ProfessorDTO
from sqlalchemy.exc import IntegrityError, NoResultFound, SQLAlchemyError
from http import HTTPStatus
from fastapi.responses import JSONResponse

class ProfessorController:

    def __init__(self):
        self.serv = ProfessorService()

    def insrt_professor_controller(self, data: ProfessorDTO):
        try:
            self.serv.insrt_professor_service(data)
        except IntegrityError:
            return JSONResponse(
                status_code=HTTPStatus.BAD_REQUEST,
                content="Bad Request"
            )
        except NoResultFound:
            return JSONResponse(
                status_code=HTTPStatus.BAD_REQUEST,
                content="Bad Request"
            )
        except SQLAlchemyError:
            return JSONResponse(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                content="Internal Error"
            )
        return {
                "status_code": HTTPStatus.CREATED,
                "content": "Formato Object Created"
            }

    def updt_professor_controller(self, data: ProfessorDTO, id: int):
        try:
            self.serv.updt_professor_service(data, id)
        except IntegrityError:
            return JSONResponse(
                status_code=HTTPStatus.BAD_REQUEST,
                content="Bad Request"
            )
        except NoResultFound:
            return JSONResponse(
                status_code=HTTPStatus.BAD_REQUEST,
                content="Bad Request"
            )
        except SQLAlchemyError:
            return JSONResponse(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                content="Internal Error"
            )
        return JSONResponse(
                status_code=HTTPStatus.OK,
                content="Formato Objected Updated"
            )