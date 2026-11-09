# from abc import ABC, abstractmethod

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from backend.modules.sala.sala_dto import SalaDTO
from backend.modules.sala.sala_controller import SalaController
from backend.modules.tipo_sala.tipo_sala_controller import TipoSalaController
from backend.modules.tipo_sala.tipo_sala_dto import TipoSalaDTO
from backend.modules.especialidade.especialidade_controller  import EspecialidadeController
from backend.modules.especialidade.especialidade_dto import EspecialidadeDTO
from backend.modules.formato.formato_controller import FormatoController
from backend.modules.formato.formato_dto import FormatoDTO
from backend.modules.disciplina.disciplina_controller import DisciplinaController
from backend.modules.disciplina.disciplina_dto import DisciplinaDTO
from backend.modules.disciplina_especialidade.disciplina_especialidade_controller import DisciplinaEspecialidadeController
from backend.modules.disciplina_especialidade.disciplina_especialidade_dto import DisciplinaEspecialidadeDTO

from router import cadastro

sala = SalaController()
tipo_sala = TipoSalaController()
especialidade = EspecialidadeController()
formato = FormatoController()
disciplina = DisciplinaController()
disciplina_especialidade = DisciplinaEspecialidadeController()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],  # endereço do Vite
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class BaseAPI(ABC):
    
# Rota de Status da API
@app.get("/api/health")
async def health_check() -> JSONResponse:
    return JSONResponse(content={"status": "ok", "message": "API operacional."})

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request, name="index.html"
    )

#----------------------ROTAS CADASTRO----------------------------

app.include_router(cadastro.router)

@app.get("/semana")
async def semana(request: Request):
    return templates.TemplateResponse(
        request, name="semana.html"
    )

@app.get("/hoje")
async def hoje(request: Request):
    return templates.TemplateResponse(
        request, name="hoje.html"
    )
    


# -------------------------------ROTAS DE SALA-----------------------------
@app.get("/sala/")
def sala_index() -> JSONResponse:
    return sala.slct_sala_controller()

@app.get("/sala/{id}")
async def sala_by_id(id: int) -> JSONResponse:
    return sala.slct_by_id_sala_controller(id)


@app.post("/sala/")
def insrt_sala(data: SalaDTO) -> JSONResponse:
    return sala.insrt_sala_controller(data)

@app.put("/sala/{id}", )
async def updt_sala(data: SalaDTO, id: int) -> JSONResponse:
    return sala.updt_sala_controller(data, id)

@app.delete("/sala/{id}")
async def del_sala(id: int) -> JSONResponse:
    return sala.del_sala_controller(id)
    
#---------------------------------------------------------------------------

#-------------------------ROTAS TIPO SALA-----------------------------------
@app.get("/tipo-sala/")
def slct_tipo_sala() -> JSONResponse:
    return tipo_sala.slct_tipo_sala_controller()

@app.get("/tipo-sala/{id}")
def slct_tipo_sala(id: int) -> JSONResponse:
    return tipo_sala.slct_by_id_tipo_sala_controller(id)

@app.post("/tipo-sala/")
def insrt_tipo_sala(data: TipoSalaDTO) -> JSONResponse:
    return tipo_sala.insrt_tipo_sala_controller(data)

@app.put("/tipo-sala/{id}")
def updt_tipo_sala(data: TipoSalaDTO, id: int) -> JSONResponse:
    return tipo_sala.updt_tipo_sala_controller(data, id)

@app.delete("/tipo-sala/{id}")
def del_tipo_sala(id: int) -> JSONResponse:
    return tipo_sala.del_tipo_sala_controller(id)
#----------------------------------------------------------------------------

#----------------------------ROTAS ESPECIALIDADE----------------------------
@app.get("/especialidade/")
def select_especialidade() -> JSONResponse:
    return especialidade.slct_especialidade_controller()

@app.get("/especialidade/{id}")
def select_by_id_especialidade(id: int) -> JSONResponse:
    return especialidade.slct_by_id_especialidade_controller(id)


@app.post("/especialidade/")
def insrt_especialidade(data: EspecialidadeDTO) -> JSONResponse:
    return especialidade.insrt_especialidade_controller(data)

@app.put("/especialidade/{id}")
def updt_especialidade(data: EspecialidadeDTO, id: int) -> JSONResponse:
    return especialidade.updt_especialidade_controller(data, id)

@app.delete("/especialidade/{id}")
def del_especialidade(id: int) -> JSONResponse:
    return especialidade.del_especialidade_controller(id)
#----------------------------------------------------------------------------

#---------------------------ROTAS FORMATO------------------------------------
@app.get("/formato/")
def select_formato() -> JSONResponse:
    return formato.slct_formato_controller()

@app.get("/formato/{id}")
def select_by_id_formato(id: int) -> JSONResponse:
    return formato.slct_by_id_formato_controller(id)

@app.post("/formato/")
def insrt_formato(data: FormatoDTO) -> JSONResponse:
    return formato.insrt_formato_controller(data)

@app.put("/formato/{id}")
def updt_formato(data: FormatoDTO, id: int) -> JSONResponse:
    return formato.updt_formato_controller(data, id)

@app.delete("/formato/{id}")
def del_formato(id: int) -> JSONResponse:
    return formato.del_formato_controller(id)
#--------------------------------------------------------------------------

#----------------------------ROTAS DISCIPLINAS-----------------------------
@app.get("/disciplina/")
def select_disciplina() -> JSONResponse:
    return disciplina.slct_disciplina_controller()

@app.get("/disciplina/{id}")
def select_by_id_disciplina(id: int) -> JSONResponse:
    return disciplina.slct_by_id_disciplina_controller(id)

@app.post("/disciplina/")
def insrt_disciplina(data: DisciplinaDTO) -> JSONResponse:
    return disciplina.insrt_disciplina_controller(data)

@app.put("/disciplina/{id}")
def updt_disciplina(data: DisciplinaDTO, id: int) -> JSONResponse:
    return disciplina.updt_disciplina_controller(data, id)

@app.delete("/disciplina/{id}")
def del_disciplina(id: int) -> JSONResponse:
    return disciplina.del_disciplina_controller(id)
#--------------------------------------------------------------------------

#------------------------ROTAS DISCIPLINA ESPECIALIDADE--------------------
@app.get("/disciplina-especialidade/")
def select_disciplina_especialidade() -> JSONResponse:
    return disciplina_especialidade.slct_disciplina_especialidade_controller()
    

@app.get("/disciplina-especialidade/{id}")
def select_by_id_disciplina(id: int) -> JSONResponse:
    return disciplina_especialidade.slct_by_id_disciplina_especialidade_controller(id)

@app.post("/disciplina-especialidade/")
def insrt_disciplina(data: DisciplinaEspecialidadeDTO) -> JSONResponse:
    return disciplina_especialidade.insrt_disciplina_especialidade_controller(data)

@app.put("/disciplina-especialidade/{id}")
def updt_disciplina(data: DisciplinaEspecialidadeDTO, id: int) -> JSONResponse:
    # return disciplina_especialidade.updt_disciplina_especialidade_controller(data, id)
    pass

@app.delete("/disciplina-especialidade/{id}")
def del_disciplina(id: int) -> JSONResponse:
    return disciplina_especialidade.del_disciplina_especialidade_controller(id)
#--------------------------------------------------------------------------

#------------------------ROTAS PROFESSOR--------------------
