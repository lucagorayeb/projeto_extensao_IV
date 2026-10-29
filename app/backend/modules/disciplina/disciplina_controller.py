from .disciplina_service import DisciplinaService
from .disciplina_dto import DisciplinaDTO
from sqlalchemy.exc import IntegrityError, NoResultFound, SQLAlchemyError
from fastapi.responses import JSONResponse
from http import HTTPStatus

class DisciplinaController:

    def __init__(self):
        self.serv = DisciplinaService()

    def slct_disciplina_controller(self) -> JSONResponse:
        try:
            data = self.serv.slct_disciplina_service()
            if len(data) == 0:
                raise Exception
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
        except Exception:
            return JSONResponse(
                status_code=HTTPStatus.NOT_FOUND,
                content="Not Found"
            )
        return JSONResponse(
            status_code=HTTPStatus.OK,
            content=data
        )

    def insrt_disciplina_controller(self, data: DisciplinaDTO) -> JSONResponse:
        try:
            self.serv.insrt_disciplina_service(data)
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
                status_code=HTTPStatus.CREATED,
                content="Disciplina Object Created"
            )

    def updt_disciplina_controller(self, data: DisciplinaDTO, id: int) -> JSONResponse:
        try:
            self.serv.updt_disciplina_service(data, id)
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
                content="Disciplina Objected Updated"
            )

    def del_disciplina_controller(self, id: int) -> JSONResponse:
        try:
            self.serv.del_disciplina_service(id)
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
                content="Disciplina Objected Deleted"
            )

    def slct_by_id_disciplina_controller(self, id: int) -> JSONResponse:
        try:
            data = self.serv.slct_by_id_disciplina_service(id)
            if len(data) == 0:
                raise Exception
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
        except Exception:
            return JSONResponse(
                status_code=HTTPStatus.NOT_FOUND,
                content="Not Found"
            )
        return JSONResponse(
                status_code=HTTPStatus.OK,
                content=data
            )