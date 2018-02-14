from django.test import TestCase

from sare.questionarios.models import Questionario


class QuestionarioDetalhe(TestCase):
    def setUp(self):
        self.obj = Questionario.objects.create(
            nome='Samuel Barbosa',
            cpf='12345678901',
            email='samuka1@gmail.com',
            cidade='Palmas'
        )
        self.resp = self.client.get('/questionario/{}/'.format(self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'questionarios/detalhes.html')

    def test_context(self):
        quest = self.resp.context['quest']
        self.assertIsInstance(quest, Questionario)

    def test_html(self):
        contents = (self.obj.nome, self.obj.cpf,
                    self.obj.email, self.obj.cidade)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class QuestionarioDetalheNaoEncontrado(TestCase):
    def test_nao_encontrado(self):
        resp = self.client.get('/inscricao/0/')
        self.assertEqual(404, resp.status_code)