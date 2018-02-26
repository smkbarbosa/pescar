from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / deve retornar status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Deve acessar o index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_questionario_link(self):
        expected = 'href="{}'.format(r('questionarios:new'))
        self.assertContains(self.response, expected)

    def test_recupera_comprovante(self):
        """Deve ter opção para recuperar comprovante na página inicial"""
        self.assertTemplateUsed(self.response, 'consulta.html')
