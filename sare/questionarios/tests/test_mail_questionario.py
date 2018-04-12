from unittest import skipIf

from django.core import mail
from django.forms import model_to_dict
from django.test import TestCase
from django.shortcuts import resolve_url as r
from model_mommy import mommy

from sare.questionarios.models import QuestionarioOld


class QuestionarioNewPostValid(TestCase):
    def setUp(self):
        self.obj = mommy.prepare(QuestionarioOld, nome='Samuel Barbosa', cpf='85472840519', email='samuka1@gmail.com',
                                 cidade='Palmas', bairro='Plano Diretor norte', origem_renda='2',
                                 fale_mais_familia='OK Teste', _fill_optional=True)

        form_fields = model_to_dict(self.obj, fields=[field.name for field in self.obj._meta.fields])

        self.data = {field: getattr(self.obj, field) for field in form_fields}

        self.resp = self.client.post(r('questionarios:new'), self.data)
        self.client.post(r('questionarios:new'), self.data)
        self.email = mail.outbox[0]

    # @skipIf('ERROR', 'Pulando enquanto o redirecionamento for para consultar')
    def test_email_questionario_assunto(self):
        expect = 'Questionário Socioeconômico preenchido com sucesso'
        self.assertEqual(expect, self.email.subject)

    # @skipIf('ERROR', 'Pulando enquanto o redirecionamento for para consultar')
    def test_email_questionario_remetente(self):
        # expect = 'pescar.gt.ss@gmail.com'
        expect = 'clae.palmas@ifto.edu.br'
        self.assertEqual(expect, self.email.from_email)

    # @skipIf('ERROR', 'Pulando enquanto o redirecionamento for para consultar')
    def test_email_questionario_para(self):
        expect = ['samuka1@gmail.com']

        self.assertEqual(expect, self.email.to)

    # @skipIf('ERROR', 'Pulando enquanto o redirecionamento for para consultar')
    def test_questionario_corpo_email(self):
        contents = [
            'Samuel Barbosa',
            'samuka1@gmail.com',
            '85472840519',
            'Palmas'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
