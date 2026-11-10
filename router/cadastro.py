from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from backend.modules.especialidade.especialidade_controller  import EspecialidadeController
# from backend.modules.especialidade.especialidade_dto import EspecialidadeDTO
from backend.modules.professor.professor_controller import ProfessorController
# from backend.modules.professor.professor_dto import ProfessorDTO
from fastapi.responses import RedirectResponse
from http import HTTPStatus

router = APIRouter()
router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Objetos Instanciados
especialidade = EspecialidadeController()
professor = ProfessorController()

@router.get("/cadastro", tags=["cadastro"])
async def cadastro(request: Request):
    return templates.TemplateResponse(
        request, name="cadastro.html"
    )

@router.get("/cadastro/professor")
async def get_especialidades(request: Request):
    especialidades = especialidade.slct_especialidade_controller()
    professores = professor.slct_professor_controller()

    return templates.TemplateResponse(
        request,
        name="components/professores.html",
        context={
            "status": "Sucesso",
            "especialidades": especialidades['content'],
            "professores": professores['content']
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

@router.delete("/cadastro/professor/")
async def delete_professor(request: Request):
    data = await request.form()
    format_data = {}
    print(data)
    for key, value in data.items():
            format_data.update({key: value})
    print(format_data)
    # professor.insrt_professor_controller(format_data)