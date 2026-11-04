from .disciplina_especialidade_service import DisciplinaEspecialidadeService
from .disciplina_especialidade_dto import DisciplinaEspecialidadeDTO
from sqlalchemy.exc import IntegrityError, NoResultFound, SQLAlchemyError
from fastapi.responses import JSONResponse
from http import HTTPStatus

class DisciplinaEspecialidadeController:

    def __init__(self):
        self.serv = DisciplinaEspecialidadeService()

    def insrt_disciplina_especialidade_controller(self, data: DisciplinaEspecialidadeDTO) -> JSONResponse:
        try:
            self.serv.insrt_disciplina_especialidade_service(data)
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
                content="Disciplina Especialidade Object Created"
            )
    
    def del_disciplina_especialidade_controller(self, id: int) -> JSONResponse:
        try:
            self.serv.del_disciplina_especialidade_service(id)
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
                content="Disciplina Especialidade Objected Deleted"
            )

    def slct_disciplina_especialidade_controller(self) -> JSONResponse:
        try:
            data = self.serv.slct_disciplina_especialidade_service()
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
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                content="Internal Error"
            )
        return JSONResponse(
            status_code=HTTPStatus.OK,
            content=data
        )

    def slct_by_id_disciplina_especialidade_controller(self, id: int) -> JSONResponse:
        try:
            data = self.serv.slct_by_id_disciplina_especialidade_service(id)
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
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                content="Internal Error"
            )
        return JSONResponse(
            status_code=HTTPStatus.OK,
            content=data
        )