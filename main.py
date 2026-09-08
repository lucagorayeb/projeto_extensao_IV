from app.backend.controllers.disciplinas_controller import (
    DisciplinasController as dc
)
from app.backend.controllers.formato_controller import (
    FormatoController as fc
)


try:
    dc.get_from_disciplinas_controller()
except Exception as e:
    print(f"Erro: {e}")

try:
    fc.get_from_formatos_controller()
except Exception as e:
    print(f"Erro: {e}")
