from datetime import datetime
from unittest import skipIf

from django.test import TestCase
from sare.questionarios.models import Questionario


class QuestionarioModelTest(TestCase):
    def setUp(self):
        self.obj = Questionario(
                nome='Samuel Barbosa',
                cpf='12345678901',
                sexo='M',
                cidade='Palmas',
        )
        self.obj.save()

    @skipIf(AssertionError, "Salvar desabilitado na view")
    def test_create(self):
        self.assertTrue(Questionario.objects.exists())

    def test_criado_em(self):
       """Questionario deve conter campo para registro de quando foi criado"""
       self.assertIsInstance(self.obj.criado_em, datetime)
