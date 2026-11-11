import unittest
from unittest.mock import patch

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient

from backend.modules.sala.sala_controller import SalaController
from router import cadastro as cadastro_sala


class CadastroSalaTests(unittest.TestCase):
    def setUp(self):
        app = FastAPI()
        app.include_router(cadastro_sala.router)
        for name in ("index", "semana", "hoje", "cadastro"):
            app.add_api_route("/" + name, lambda: None, name=name)
        self.client = TestClient(app)
        self.salas = patch.object(cadastro_sala.sala, "slct_sala_controller").start()
        self.tipos = patch.object(cadastro_sala.tipo_sala, "slct_tipo_sala_controller").start()
        self.addCleanup(patch.stopall)
        self.salas.return_value = JSONResponse(content=[])
        self.tipos.return_value = JSONResponse(content=[{"id": 1, "tipo_sala": "Laboratório"}])

    def test_renderiza_salas_e_tipos_do_banco(self):
        self.salas.return_value = JSONResponse(content=[{
            "id": 7,
            "nome_sala": "LAB <02>",
            "quantidade_alunos": 30,
            "tipo_sala_id": 1,
            "tipo_sala": "Laboratório",
        }])
        response = self.client.get("/cadastro/sala")
        self.assertEqual(response.status_code, 200)
        self.assertIn('data-id="7"', response.text)
        self.assertIn("LAB &lt;02&gt;", response.text)
        self.assertIn('data-capacidade="30"', response.text)
        self.assertIn('value="Laboratório" data-id="1"', response.text)

    def test_renderiza_lista_vazia(self):
        response = self.client.get("/cadastro/sala")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Nenhuma sala cadastrada", response.text)

    def test_formulario_e_modais_seguem_campos_de_sala(self):
        response = self.client.get("/cadastro/sala")
        self.assertIn('id="btnCadastrarSala"', response.text)
        for modal in ("view-sala-modal", "edit-sala-modal", "delete-sala-modal"):
            self.assertIn('id="' + modal + '"', response.text)
        for field in ("nome", "tipo", "capacidade"):
            self.assertIn('name="' + field + '"', response.text)
        for field in ("predio", "andar"):
            self.assertNotIn('name="' + field + '"', response.text)
        self.assertNotIn('data-action="add-specialty"', response.text)

    def test_listagem_preserva_capacidade_zero(self):
        self.salas.return_value = JSONResponse(content=[{
            "id": 1, "nome_sala": "Virtual", "tipo_sala": "Ambiente virtual",
            "quantidade_alunos": 0,
        }])
        response = self.client.get("/cadastro/sala")
        self.assertIn('data-sala-capacidade>0</span>', response.text)

    def test_renderiza_sem_tipos(self):
        self.tipos.return_value = JSONResponse(content=[])
        response = self.client.get("/cadastro/sala")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Nenhum tipo de ambiente cadastrado", response.text)

    def test_preserva_erro_na_consulta_de_salas(self):
        self.salas.return_value = JSONResponse(status_code=500, content="Internal Error")
        response = self.client.get("/cadastro/sala")
        self.assertEqual(response.status_code, 500)
        self.tipos.assert_not_called()

    def test_preserva_erro_na_consulta_de_tipos(self):
        self.tipos.return_value = JSONResponse(status_code=500, content="Internal Error")
        response = self.client.get("/cadastro/sala")
        self.assertEqual(response.status_code, 500)

    def test_controller_aceita_lista_vazia(self):
        controller = SalaController()
        with patch.object(controller.ctrl, "slct_sala_service", return_value=[]):
            response = controller.slct_sala_controller()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.body, b"[]")


if __name__ == "__main__":
    unittest.main()
