from app.backend.modules.sala.sala_controller import SalaController
c = SalaController()

data = {
    "numero_nom": "Sala 400",
    "limite_alunos": 40,
    "fk_tipo_sala": 4
}

def insert_sala():
    c.insrt_sala_controller(data)