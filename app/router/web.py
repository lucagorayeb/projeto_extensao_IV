from fastapi import FastAPI
from http import HTTPStatus
from fastapi.responses import JSONResponse
from ..backend.modules.sala.sala_controller import SalaController
from ..backend.modules.sala.sala_dto import SalaDTO
from ..backend.modules.tipo_sala.tipo_sala_controller import TipoSalaController
from ..backend.modules.tipo_sala.tipo_sala_dto import TipoSalaDTO
from ..backend.modules.especialidade.especialidade_controller  import EspecialidadeController
from ..backend.modules.especialidade.especialidade_dto import EspecialidadeDTO
from ..backend.modules.formato.formato_controller import FormatoController
from ..backend.modules.formato.formato_dto import FormatoDTO
from ..backend.modules.disciplina.disciplina_controller import DisciplinaController
from ..backend.modules.disciplina.disciplina_dto import DisciplinaDTO

sala = SalaController()
tipo_sala = TipoSalaController()
especialidade = EspecialidadeController()
formato = FormatoController()
disciplina = DisciplinaController()
app = FastAPI()


# Rota Principal
@app.get("/")
async def index() -> JSONResponse:
    return {"message": "Hello World."}


# -------------------------------ROTAS DE SALA-----------------------------
@app.get("/sala/")
def sala_index() -> JSONResponse:
    return sala.slct_sala_controller()

@app.get("/sala/{id}")
async def sala_by_id(id: int) -> JSONResponse:
    return sala.slct_by_id_sala_controller(id)


@app.post("/sala/")
async def insrt_sala(data: SalaDTO) -> JSONResponse:
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
