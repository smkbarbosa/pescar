from datetime import datetime
from unittest import skipIf

from django.test import TestCase
from model_mommy import mommy

from sare.questionarios.models import Questionario


class QuestionarioModelTest(TestCase):
    def setUp(self):
        # self.obj = Questionario(
        #         nome='Samuel Barbosa',
        #         cpf='12345678901',
        #         sexo='M',
        #         cidade='Palmas',
        #         email='samuka1@gmail.com'
        # )
        self.obj = mommy.make(Questionario, nome='Samuel Barbosa', cpf='65673063008', _fill_optional=True )
        self.obj.save()


#     # @skipIf(AssertionError, "Salvar desabilitado na view")
    def test_create(self):
        self.assertTrue(Questionario.objects.exists())

    def test_criado_em(self):
        """Questionario deve conter campo para registro de quando foi criado"""
        self.assertIsInstance(self.obj.criado_em, datetime)

    # @skipIf(AssertionError, "utilizando mommy model")
    def test_str(self):
        self.assertEqual('Samuel Barbosa', str(self.obj))
