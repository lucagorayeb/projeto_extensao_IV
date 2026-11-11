import unittest
from html.parser import HTMLParser
from unittest.mock import patch

from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient

from router import cadastro
from router.web import app


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.links.append(dict(attrs).get("href", ""))


class CadastroNavegacaoTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_links_de_cadastro_abrem_as_paginas(self):
        with (
            patch.object(cadastro.sala, "slct_sala_controller", return_value=JSONResponse(content=[])),
            patch.object(cadastro.tipo_sala, "slct_tipo_sala_controller", return_value=JSONResponse(content=[])),
            patch.object(cadastro.especialidade, "slct_especialidade_controller", return_value={"status_code": 200, "content": []}),
            patch.object(cadastro.professor, "slct_professor_controller", return_value={"status_code": 200, "content": []}),
            patch.object(cadastro.professor_especialidade, "slct_professor_especialidade_controller", return_value=[]),
        ):
            response = self.client.get("/cadastro")
            self.assertEqual(response.status_code, 200)
            parser = LinkParser()
            parser.feed(response.text)
            self.assertFalse(any("url_for(" in link for link in parser.links))
            for path, title in (("/cadastro/sala", "Salas"), ("/cadastro/professor", "Professores")):
                url = "http://testserver" + path
                self.assertIn(url, parser.links)
                page = self.client.get(url)
                self.assertEqual(page.status_code, 200)
                self.assertIn('<h1 class="page-title">' + title + '</h1>', page.text)

    def test_erro_de_especialidade_nao_causa_erro_de_template(self):
        with patch.object(cadastro.especialidade, "slct_especialidade_controller", return_value=JSONResponse(status_code=503, content="Indisponível")):
            response = self.client.get("/cadastro/professor")
        self.assertEqual(response.status_code, 503)

    def test_erro_de_professor_e_preservado(self):
        with (
            patch.object(cadastro.especialidade, "slct_especialidade_controller", return_value={"status_code": 200, "content": []}),
            patch.object(cadastro.professor, "slct_professor_controller", return_value=JSONResponse(status_code=500, content="Internal Error")),
        ):
            response = self.client.get("/cadastro/professor")
        self.assertEqual(response.status_code, 500)


if __name__ == "__main__":
    unittest.main()
