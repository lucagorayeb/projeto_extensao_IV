import json

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

router = APIRouter()
router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Objetos Instanciados
especialidade = EspecialidadeController()
professor = ProfessorController()
professor_especialidade = ProfessorEspecialidadeController()
sala = SalaController()
tipo_sala = TipoSalaController()

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
    professores_especialidades = professor_especialidade.slct_professor_especialidade_controller()

    return templates.TemplateResponse(
        request,
        name="components/professores.html",
        context={
            "status": "Sucesso",
            "especialidades": especialidades['content'],
            "professores": professores['content'],
            "professores_especialidades": professores_especialidades
        }
    )

@router.post("/cadastro/professor")
async def insert_professor(request: Request) -> RedirectResponse:
    data = await request.form()
    format_data = {}
    for key, value in data.items():
        format_data.update({key: value})

    professor.insrt_professor_controller(format_data)
    return RedirectResponse(
        url="/cadastro/professor", 
        status_code=HTTPStatus.SEE_OTHER
    )

@router.put("/cadastro/professor")
async def update_professor(request: Request):
    data = await request.form()
    try:
        professor_id = int(data.get("id", ""))
    except (TypeError, ValueError):
        return JSONResponse(status_code=HTTPStatus.BAD_REQUEST, content="Professor inválido.")

    nome = str(data.get("nome", "")).strip()
    cpf = str(data.get("cpf", "")).strip()
    if professor_id <= 0 or not nome or not cpf:
        return JSONResponse(status_code=HTTPStatus.BAD_REQUEST, content="Informe o nome e o CPF do professor.")

    return professor.updt_professor_controller({"nome": nome, "cpf": cpf}, professor_id)


@router.delete("/cadastro/professor/")
async def delete_professor(request: Request):
    data = await request.form()
    format_data = {}

    for key, value in data.items():
        format_data.update({key: value})

    result = professor.del_professor_controller(format_data)
    if isinstance(result, JSONResponse):
        return result

    return RedirectResponse(
        url="/cadastro/professor",
        status_code=HTTPStatus.SEE_OTHER
    )

@router.post("/cadastro/professor/especialidade")
async def insert_especialidade_professor(request: Request):
    data = await request.form()
    format_data = {}

    for key, value in data.items():
        format_data.update({key: value})

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
    if salas.status_code >= HTTPStatus.BAD_REQUEST:
        return salas

    tipos_sala = tipo_sala.slct_tipo_sala_controller()
    if tipos_sala.status_code >= HTTPStatus.BAD_REQUEST:
        return tipos_sala

    return templates.TemplateResponse(
        request,
        name="components/salas.html",
        context={
            "status": "Sucesso",
            "salas": json.loads(salas.body),
            "tipos_sala": json.loads(tipos_sala.body),
        }
    )
