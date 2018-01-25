from django.core import mail
from django.test import TestCase


class Questionario_Post_Valid(TestCase):
    def setUp(self):
        data = dict(nome='Samuel Barbosa', cpf='12345678901',
                    email='samuka1@gmail.com',
                    cidade='Palmas')
        self.client.post('/questionario/', data)
        self.email = mail.outbox[0]

    # @skipIf(IndexError, 'Descobrir o motivo depois')
    def test_email_questionario_assunto(self):
        expect = 'Questionário Socioeconômico preenchido com sucesso'

        self.assertEqual(expect, self.email.subject)

    # @skipIf(IndexError, 'Descobrir o motivo depois')
    def test_email_questionario_remetente(self):
        expect = 'pescar.gt.ss@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    # @skipIf(IndexError, 'Descobrir o motivo depois')
    def test_email_questionario_para(self):
        expect = ['samuka1@gmail.com',]

        self.assertEqual(expect, self.email.to)

    # @skipIf(IndexError, 'Descobrir o motivo depois')
    def test_questionario_corpo_email(self):
        contents = [
            'Samuel Barbosa',
            'samuka1@gmail.com',
            '12345678901',
            'Palmas'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

    # def test_salva_questionario(self):
    #    self.assertTrue(Questionario.objects.exists())
    #   pass