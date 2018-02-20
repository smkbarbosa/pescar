from django.test import TestCase
from django.shortcuts import resolve_url as r
from model_mommy import mommy

from sare.questionarios.models import Questionario


class QuestionarioDetalhe(TestCase):
    def setUp(self):
        # self.obj = Questionario.objects.create(
        #     nome='Samuel Barbosa',
        #     cpf='12345678901',
        #     email='samuka1@gmail.com',
        #     cidade='Palmas'
        # )
        self.obj = mommy.make(Questionario, cpf='12345678901', nome='Samuel Barbosa', cidade='Palmas',
                              email='samuka1@gmail.com', _fill_optional=True)
        self.resp = self.client.get(r('questionarios:detalhe', self.obj.hashId))

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
        resp = self.client.get(r('questionarios:detalhe', '00000000-0000-0000-0000-000000000000'))
        self.assertEqual(404, resp.status_code)