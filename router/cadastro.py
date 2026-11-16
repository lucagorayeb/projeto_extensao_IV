import json
import logging
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from backend.modules.especialidade.especialidade_controller  import EspecialidadeController
from backend.modules.professor.professor_controller import ProfessorController
from backend.modules.professor_especialidade.professor_especialidade_controller import ProfessorEspecialidadeController
from fastapi.responses import JSONResponse, RedirectResponse
from http import HTTPStatus
from backend.modules.sala.sala_controller import SalaController
from backend.modules.tipo_sala.tipo_sala_controller import TipoSalaController
from backend.modules.utils.requests_treatment import request_treatment
from backend.modules.turma.turma_controller import TurmaController
from backend.modules.disciplina.disciplina_controller import DisciplinaController
from backend.modules.disciplina.disciplina_dto import DisciplinaDTO
from backend.modules.formato.formato_controller import FormatoController
from pydantic import ValidationError
from backend.modules.turma.turma_exception import ScheduleConflict, ProfessorClassNumber, ProfessorScheduleConflict
from fastapi import HTTPException

router = APIRouter()
router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Objetos Instanciados
especialidade = EspecialidadeController()
professor = ProfessorController()
professor_especialidade = ProfessorEspecialidadeController()
sala = SalaController()
tipo_sala = TipoSalaController()
turma = TurmaController()
disciplina = DisciplinaController()
formato = FormatoController()

@router.get("/cadastro", tags=["cadastro"])
async def cadastro(request: Request):
    return templates.TemplateResponse(
        request, name="cadastro.html"
    )

@router.get("/cadastro/professor", tags=['cadastro'])
async def index_cadastro_professor(request: Request):
    especialidades = especialidade.slct_especialidade_controller()

    if isinstance(especialidades, JSONResponse):
        return especialidades
    
    professores = professor.slct_professor_controller()
    
    if isinstance(professores, JSONResponse):
        return professores
    
    if professores["status_code"] >= HTTPStatus.BAD_REQUEST:
        return JSONResponse(status_code=professores["status_code"], content=professores["content"])
    # professores_especialidades = professor_especialidade.slct_by_id_professor_especialidade_controller()
    # print(professores_especialidades)

    return templates.TemplateResponse(
        request,
        name="components/professores.html",
        context={
            "status": "Sucesso",
            "especialidades": especialidades['content'],
            "professores": professores['content'],
        }
    )

@router.post("/cadastro/professor")
async def insert_professor(request: Request) -> RedirectResponse:
    data = await request.form()
    format_data = request_treatment(data)
    professor.insrt_professor_controller(format_data)
    return RedirectResponse(
        url="/cadastro/professor", 
        status_code=HTTPStatus.SEE_OTHER
    )

@router.put("/cadastro/professor")
async def update_professor(request: Request):
    data = await request.form()
    professor_id = int(data.get("id", ""))

    nome = str(data.get("nome", "")).strip()
    cpf = str(data.get("cpf", "")).strip()

    if professor_id <= 0 or not nome or not cpf:
        return JSONResponse(status_code=HTTPStatus.BAD_REQUEST, content="Informe o nome e o CPF do professor.")

    return professor.updt_professor_controller({"nome": nome, "cpf": cpf}, professor_id)


@router.delete("/cadastro/professor/")
async def delete_professor(request: Request):
    data = await request.form()
    format_data = request_treatment(data)
    result = professor.del_professor_controller(format_data)
    if isinstance(result, JSONResponse):
        return result

    return RedirectResponse(
        url="/cadastro/professor",
        status_code=HTTPStatus.SEE_OTHER
    )

@router.get("/cadastro/professor/especialidade")
async def get_especialidade_professor(request: Request):
    pass

@router.get("/cadastro/professor/especialidade/{id}")
async def get_by_id_especialidade_professor(id: int):
    return professor_especialidade.slct_by_id_professor_especialidade_controller(id)


@router.post("/cadastro/professor/especialidade")
async def insert_especialidade_professor(request: Request):
    data = await request.form()
    format_data = request_treatment(data)
    result = professor_especialidade.insrt_professor_especialidade_controller(format_data)

    if isinstance(result, JSONResponse):
        return result
    if result["status_code"] >= HTTPStatus.BAD_REQUEST:
        return JSONResponse(status_code=result["status_code"], content=result["content"])

    return RedirectResponse(
        url="/cadastro/professor",
        status_code=HTTPStatus.SEE_OTHER
    )

# SALA

@router.get("/cadastro/sala")
async def index_cadastro_sala(request: Request):
    salas = sala.slct_sala_controller()
    if salas['status_code'] >= HTTPStatus.BAD_REQUEST:
        return salas

    tipos_sala = tipo_sala.slct_tipo_sala_controller()
    if tipos_sala['status_code'] >= HTTPStatus.BAD_REQUEST:
        return tipos_sala
    
    return templates.TemplateResponse(
        request,
        name="components/salas.html",
        context={
            "status": "Sucesso",
            "salas": salas['content'],
            "tipos_sala": tipos_sala['content'],
        }
    )

@router.post("/cadastro/sala/")
async def insrt_sala(request: Request):
    data = await request.form()
    format_data = request_treatment(data)
    sala.insrt_sala_controller(format_data)
    return RedirectResponse(
        url="/cadastro/sala", 
        status_code=HTTPStatus.SEE_OTHER
    )

@router.delete("/cadastro/sala/")
async def del_sala(request: Request):
    data = await request.form()
    format_data = request_treatment(data)
    sala.del_sala_controller(format_data)
    return RedirectResponse(
        url="/cadastro/sala", 
        status_code=HTTPStatus.SEE_OTHER
    )

@router.put("/cadastro/sala")
async def update_sala(request: Request):
    data = await request.form()
    try:
        sala_id = int(data.get("id", ""))
        fk_tipo_sala = int(data.get("fk_tipo_sala", ""))
        limite_alunos = int(data.get("limite_alunos", ""))
    except (TypeError, ValueError):
        return JSONResponse(status_code=HTTPStatus.BAD_REQUEST, content="Informe uma sala, um tipo e uma capacidade válidos.")

    nome = str(data.get("nome", "")).strip()
    if sala_id <= 0 or not nome or fk_tipo_sala <= 0 or limite_alunos < 0:
        return JSONResponse(status_code=HTTPStatus.BAD_REQUEST, content="Informe o nome, o tipo da sala e uma capacidade não negativa.")

    return sala.updt_sala_controller({"nome": nome, "fk_tipo_sala": fk_tipo_sala, "limite_alunos": limite_alunos}, sala_id)

# TURMA 

@router.get("/cadastro/turma")
async def index_turma(request: Request):

    turmas = turma.slct_turma_controller()
    disciplinas = disciplina.slct_disciplina_controller()
    professores = professor.slct_professor_controller()
    salas = sala.slct_sala_controller()
    dias_semana = turma.get_dias_semana_controller()
    

    return templates.TemplateResponse(
        request,
        name="components/turmas.html",
        context={
            "status": "Sucesso",
            "turmas": turmas,
            "disciplinas": disciplinas["content"],
            "professores": professores['content'],
            "salas": salas['content'],
            "dias_semana": dias_semana
        }
    )

@router.post("/cadastro/turma")
async def cadastrar_turma(request: Request):
    data = await request.form()
    format_data = request_treatment(data)
    
    try:
        turma.insrt_turma_controller(format_data)
    except (ScheduleConflict, ProfessorClassNumber, ProfessorScheduleConflict) as error:
        raise HTTPException(status_code=409, detail=str(error)) from error
    except IntegrityError as error:
        raise HTTPException(
            status_code=422,
            detail="Não foi possível cadastrar a turma. Verifique se a disciplina, o professor, a sala e o dia selecionados ainda estão disponíveis.",
        ) from error
    except SQLAlchemyError as error:
        logging.getLogger(__name__).exception("Erro ao cadastrar turma")
        raise HTTPException(status_code=500, detail="Não foi possível cadastrar a turma. Tente novamente mais tarde.") from error
    
    return RedirectResponse(
        url = "/cadastro/turma", 
        status_code = HTTPStatus.SEE_OTHER
    )

@router.put("/cadastro/turma")
async def atualizar_turma(request: Request):
    data = await request.form()
    format_data = request_treatment(data)

    try:
        turma_id = int(format_data.pop("id", ""))
        if turma_id <= 0:
            raise ValueError
    except (TypeError, ValueError) as error:
        raise HTTPException(status_code=422, detail="Informe uma turma válida para atualizar.") from error

    try:
        turma.updt_turma_controller(format_data, turma_id)
    except (ScheduleConflict, ProfessorClassNumber, ProfessorScheduleConflict) as error:
        raise HTTPException(status_code=409, detail=str(error)) from error
    except IntegrityError as error:
        raise HTTPException(
            status_code=422,
            detail="Não foi possível atualizar a turma. Verifique se a disciplina, o professor, a sala e o dia selecionados ainda estão disponíveis.",
        ) from error
    except SQLAlchemyError as error:
        logging.getLogger(__name__).exception("Erro ao cadastrar turma")
        raise HTTPException(status_code=500, detail="Não foi possível atualizar a turma. Tente novamente mais tarde.") from error
    
    return RedirectResponse(
        url = "/cadastro/turma", 
        status_code = HTTPStatus.SEE_OTHER
    )

@router.delete("/cadastro/turma/{id}")
async def delete_turma(id: int):
    try:
        turma.del_turma_controller(id)
    except IntegrityError as error:
        raise HTTPException(
            status_code=422,
            detail="Não foi possível remover a turma.",
        ) from error
    except SQLAlchemyError as error:
        logging.getLogger(__name__).exception("Erro ao cadastrar turma")
        raise HTTPException(status_code=500, detail="Não foi possível remover a turma. Tente novamente mais tarde.") from error
    
    return RedirectResponse(
        url = "/cadastro/turma", 
        status_code = HTTPStatus.SEE_OTHER
    )
    

# DISCIPLINA
@router.get("/cadastro/disciplina")
async def index_disciplina(request: Request):
    disciplinas = disciplina.slct_disciplina_controller()
    if disciplinas["status_code"] >= HTTPStatus.BAD_REQUEST:
        raise HTTPException(status_code=disciplinas["status_code"], detail="Não foi possível carregar as disciplinas.")
    formatos = formato.slct_formato_controller()
    if formatos.status_code >= HTTPStatus.BAD_REQUEST:
        raise HTTPException(status_code=formatos.status_code, detail="Não foi possível carregar os formatos.")

    return templates.TemplateResponse(
        request,
        name="components/disciplinas.html",
        context={
            "status": "Sucesso",
            "disciplinas": disciplinas["content"],
            "formatos": json.loads(formatos.body),
        }
    )

def disciplina_form_data(data):
    values = request_treatment(data)
    values["nome"] = str(values.get("nome", "")).strip()
    try:
        result = DisciplinaDTO.model_validate(values)
        if not result.nome or len(result.nome) > 50 or result.fk_formato <= 0 or not 0 <= result.carga_horaria <= 999.99 or result.pratica not in (0, 1):
            raise ValueError
        return result
    except (ValidationError, ValueError) as error:
        raise HTTPException(status_code=422, detail="Informe nome, formato, carga horária e indicação de prática válidos.") from error


@router.post("/cadastro/disciplina")
async def cadastrar_disciplina(request: Request):
    data = await request.form()
    format_data = disciplina_form_data(data)
    
    try:
        result = disciplina.insrt_disciplina_controller(format_data)
        if result["status_code"] >= HTTPStatus.BAD_REQUEST:
            raise HTTPException(status_code=result["status_code"], detail="Não foi possível cadastrar a disciplina. Verifique os dados e tente novamente.")
    except IntegrityError as error:
        raise HTTPException(
            status_code=422,
            detail="Não foi possível cadastrar a disciplina.",
        ) from error
    except SQLAlchemyError as error:
        logging.getLogger(__name__).exception("Erro ao cadastrar disciplina")
        raise HTTPException(status_code=500, detail="Não foi possível cadastrar a disciplina. Tente novamente mais tarde.") from error
    
    return RedirectResponse(
        url = "/cadastro/disciplina", 
        status_code = HTTPStatus.SEE_OTHER
    )

@router.put("/cadastro/disciplina/{id}")
async def atualizar_disciplina(request: Request, id: int):
    data = await request.form()
    format_data = disciplina_form_data(data)
    
    try:
        result = disciplina.updt_disciplina_controller(format_data, id)
        if result["status_code"] >= HTTPStatus.BAD_REQUEST:
            raise HTTPException(status_code=result["status_code"], detail="Não foi possível atualizar a disciplina. Verifique os dados e tente novamente.")
    except IntegrityError as error:
        raise HTTPException(
            status_code=422,
            detail="Não foi possível atualizar a disciplina.",
        ) from error
    except SQLAlchemyError as error:
        logging.getLogger(__name__).exception("Erro ao atualizar disciplina")
        raise HTTPException(status_code=500, detail="Não foi possível atualizar a disciplina. Tente novamente mais tarde.") from error
    
    return RedirectResponse(
        url = "/cadastro/disciplina", 
        status_code = HTTPStatus.SEE_OTHER
    )

@router.delete("/cadastro/disciplina/{id}")
async def delete_disciplina(id: int):
    try:
        result = disciplina.del_disciplina_controller(id)
        if result["status_code"] >= HTTPStatus.BAD_REQUEST:
            raise HTTPException(status_code=result["status_code"], detail="Não foi possível remover a disciplina. Verifique se ela está vinculada a turmas ou especialidades.")
    except IntegrityError as error:
        raise HTTPException(
            status_code=422,
            detail="Não foi possível remover a disciplina.",
        ) from error
    except SQLAlchemyError as error:
        logging.getLogger(__name__).exception("Erro ao remover disciplina")
        raise HTTPException(status_code=500, detail="Não foi possível remover a disciplina. Tente novamente mais tarde.") from error
    
    return RedirectResponse(
        url = "/cadastro/disciplina",
        status_code = HTTPStatus.SEE_OTHER
    )
