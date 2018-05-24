from django.test import TestCase
from django.shortcuts import resolve_url as r
from model_mommy import mommy

from sare.questionarios.models import QuestionarioOld


class ConsultaComprovante(TestCase):
    def setUp(self):
        # self.obj = Questionario.objects.create(
        #       cpf='12345678901',
        #      email='samuka1@gmail.com',
        #      cidade='Palmas'
        #  )
        self.obj = mommy.make(QuestionarioOld, nome='Samuel Barbosa', cpf='31882451309', matricula='78',
                              _fill_optional=True)

        self.consulta = QuestionarioOld.objects.filter(cpf=self.obj.cpf, matricula=self.obj.matricula)
        self.resp = self.client.get(r('questionarios:detalhe', self.obj.hashId))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'questionarios/detalhes.html')

    def test_context(self):
        quest = self.resp.context['quest']
        self.assertIsInstance(quest, QuestionarioOld)

    def test_html(self):
        contents = (self.obj.cpf, self.obj.matricula)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class ComprovanteNaoEncontrado(TestCase):
    def test_comprovante_nao_encontrado(self):

        self.consulta = QuestionarioOld.objects.filter(cpf='46587931245', matricula='77')
        # resp = self.client.post(r('questionarios:detalhe', '00000000-0000-0000-0000-000000000000'))

        resp = self.client.get(r('questionarios:detalhe', '00000000-0000-0000-0000-000000000000'))
        self.assertEqual(404, resp.status_code)