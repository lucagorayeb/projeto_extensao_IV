from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from backend.modules.especialidade.especialidade_controller  import EspecialidadeController
from backend.modules.especialidade.especialidade_dto import EspecialidadeDTO
from backend.modules.professor.professor_controller import ProfessorController
from backend.modules.professor.professor_dto import ProfessorDTO

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
    data = especialidade.slct_especialidade_controller()
    return templates.TemplateResponse(
        request,
        name="components/professores.html",
        context={
            "status_code": data['status_code'],
            "especialidades": data['content']
        }
    )

@router.post("/cadastro/professor")
async def insert_professor(request: Request):
    data = await request.form()
    format_data = {}
    for key, value in data.items():
        format_data.update({key: value})

    response = professor.insrt_professor_controller(format_data)
    
    return templates.TemplateResponse(
        request,
        name="components/professores.html",
        context={
            "status_code": response['status_code'],
            "description": response['content']
        }
    )