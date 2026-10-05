from app.backend.modules.tipo_sala.tipo_sala_controller import TipoSalaController

tipos_sala = [
    "Laboratório de Química",
    "Laboratório de Informática",
    "Laboratório de Engenharia",
    "Sala de Aula"
]

def insert_tipo_sala():
    ctrl = TipoSalaController()

    for sala in tipos_sala:
        data = {"nome": sala}
        ctrl.insrt_tipo_sala_controller(data)