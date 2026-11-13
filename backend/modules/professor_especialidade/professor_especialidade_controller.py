from backend.modules.professor_especialidade.professor_especialidade_dto import ProfessorEspecialidadeDTO
from backend.modules.professor_especialidade.professor_especialidade_service import ProfessorEspecialidadeService
from sqlalchemy.exc import IntegrityError, NoResultFound, SQLAlchemyError
from http import HTTPStatus


class ProfessorEspecialidadeController:

    def __init__(self):
        self.serv = ProfessorEspecialidadeService()

    def insrt_professor_especialidade_controller(self, data: dict) -> dict:
        try:
            self.serv.insrt_professor_especialidade_service(data)
        except IntegrityError:
            return {
                "status_code":HTTPStatus.BAD_REQUEST,
                "content":"Bad Request"
            }
        except NoResultFound:
            return {
                "status_code":HTTPStatus.BAD_REQUEST,
                "content":"Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
                "content": "Internal Error"
            }
        return {
                "status_code": HTTPStatus.CREATED,
                "content": "Professor Object Created"
            }

    def del_professor_especialidade_controller(self, data: dict) -> dict:
        try:
            self.serv.del_professor_especialidade_service(data)
        except IntegrityError:
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content": "Bad Request"
            }
        except NoResultFound:
            return {
                "status_code": HTTPStatus.BAD_REQUEST,
                "content":"Bad Request"
            }
        except SQLAlchemyError:
            return {
                "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
                "content":"Internal Error"
            }
        return {
            "status_code": HTTPStatus.OK,
            "content": "Especialidade Objected Deleted"
        }

    def slct_professor_especialidade_controller(self) -> list:
        return self.serv.slct_professor_especialidade_service()

    def slct_by_id_professor_especialidade_controller(self, id: int) -> list:
        return self.serv.slct_by_id_professor_especialidade_service(id)
