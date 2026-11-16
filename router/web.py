# from abc import ABC, abstractmethod

from datetime import date, datetime

from fastapi import FastAPI, Request, HTTPException
from sqlalchemy.exc import SQLAlchemyError
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
from backend.modules.turma.turma_controller import TurmaController

sala = SalaController()
tipo_sala = TipoSalaController()
especialidade = EspecialidadeController()
formato = FormatoController()
disciplina = DisciplinaController()
disciplina_especialidade = DisciplinaEspecialidadeController()
turma = TurmaController()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# class BaseAPI(ABC):
    
# Rota de Status da API
@app.get("/api/health")
async def health_check() -> JSONResponse:
    return JSONResponse(content={"status": "ok", "message": "API operacional."})

@app.get("/")
async def index(request: Request):
    try:
        turmas = turma.slct_turma_controller()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=503, detail='Não foi possível carregar as turmas do painel. Tente novamente.') from error
    agora = datetime.now()
    dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
    turmas_hoje = [aula for aula in turmas if aula['fk_dia_semana_nome'] == dias[agora.weekday()]]
    proximas_aulas = [
        {**aula, 'hi': horario(aula.get('horario_inicio')), 'hf': horario(aula.get('horario_fim'))}
        for aula in turmas_hoje
        if aula.get('horario_inicio') is not None and horario(aula['horario_inicio']) >= agora.strftime('%H:%M')
    ]
    proximas_aulas.sort(key=lambda aula: (aula['hi'], aula['fk_disciplina_nome']))
    return templates.TemplateResponse(
        request,
        name="index.html",
        context={
            'turmas': turmas,
            'eventos_calendario': eventos_calendario(turmas),
            'total_turmas_hoje': len(turmas_hoje),
            'total_salas_hoje': len({aula['fk_sala'] for aula in turmas_hoje}),
            'total_professores_ativos': len({aula['fk_professor'] for aula in turmas}),
            'proximas_aulas': proximas_aulas,
        },
    )

def eventos_calendario(aulas):
    dias = {'Domingo': 0, 'Segunda-feira': 1, 'Terça-feira': 2, 'Quarta-feira': 3, 'Quinta-feira': 4, 'Sexta-feira': 5, 'Sábado': 6}
    eventos = []
    for aula in aulas:
        dia = dias.get(aula['fk_dia_semana_nome'])
        inicio, fim = aula.get('horario_inicio'), aula.get('horario_fim')
        if dia is None or inicio is None or fim is None:
            continue
        eventos.append({
            'id': str(aula['id']),
            'title': aula['fk_disciplina_nome'],
            'daysOfWeek': [dia],
            'startTime': ':'.join(parte.zfill(2) for parte in str(inicio).split(':')),
            'endTime': ':'.join(parte.zfill(2) for parte in str(fim).split(':')),
            'allDay': False,
            'extendedProps': {
                'professor': aula['fk_professor_nome'],
                'sala': aula['fk_sala_nome'],
            },
        })
    return eventos

def horario(valor):
    if valor is None:
        return ''
    partes = str(valor).split(':')
    return ':'.join(parte.zfill(2) for parte in partes[:2])

#----------------------ROTAS CADASTRO----------------------------
app.include_router(cadastro.router)
#----------------------------------------------------------------

@app.get("/semana")
async def semana(request: Request):
    dias = sorted(turma.get_dias_semana_controller(), key=lambda dia: (dia['nome'] == 'Domingo', dia['id']))
    grade = {
        dia['id']: {**dia, 'turmas': [], 'faixas': {faixa: [] for faixa in ('matutino', 'vespertino', 'noturno', 'sem_horario')}}
        for dia in dias
    }
    for aula in turma.slct_turma_controller():
        dia = grade.get(aula['fk_dia_semana'])
        if dia is None:
            continue
        inicio = aula.get('horario_inicio')
        fim = aula.get('horario_fim')
        hi, hf = horario(inicio), horario(fim)
        faixa = 'sem_horario' if not hi else 'matutino' if hi < '12:00' else 'vespertino' if hi < '18:00' else 'noturno'
        card = {**aula, 'hi': hi, 'hf': hf}
        dia['turmas'].append(card)
        dia['faixas'][faixa].append(card)
    for dia in grade.values():
        dia['turmas'].sort(key=lambda aula: (aula['hi'] or '99:99', aula['fk_disciplina_nome']))
        for aulas in dia['faixas'].values():
            aulas.sort(key=lambda aula: (aula['hi'] or '99:99', aula['fk_disciplina_nome']))
    return templates.TemplateResponse(
        request, name="semana.html", context={'dias': list(grade.values())}
    )

@app.get("/hoje")
async def hoje(request: Request):
    data_atual = date.today()
    dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
    meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
    dia_atual = dias[data_atual.weekday()]
    aulas = [
        {**aula, 'hi': horario(aula.get('horario_inicio')), 'hf': horario(aula.get('horario_fim'))}
        for aula in turma.slct_turma_controller()
        if aula['fk_dia_semana_nome'] == dia_atual
    ]
    aulas.sort(key=lambda aula: (aula['hi'] or '99:99', aula['fk_disciplina_nome']))
    return templates.TemplateResponse(
        request, name="hoje.html", context={
            'turmas': aulas,
            'data_descricao': f'{dia_atual}, {data_atual.day:02d} de {meses[data_atual.month - 1]} de {data_atual.year}',
        }
    )

# -------------------------------ROTAS DE SALA-----------------------------
@app.get("/sala/")
def sala_index() -> JSONResponse:
    return sala.slct_sala_controller()

@app.get("/sala/{id}")
async def sala_by_id(id: int) -> JSONResponse:
    return sala.slct_by_id_sala_controller(id)


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
