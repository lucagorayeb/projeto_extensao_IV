from app.backend.modules.formato.formato_controller import FormatoController


def teste_conexao_bd():
    ctrl = FormatoController()
    result = ctrl.slct_by_id_formato_controller(2)
    for key, value in result:
        assert key == 2
