from datetime import datetime

from django.test import TestCase
from model_mommy import mommy

from sare.core.models import Aluno
from sare.questionarios.models import QuestionarioOld, Questionario, DimensaoEconomica, DimensaoSocial, \
    DimensaoCultural, DimensaoAmbiental


class QuestionarioOldModelTest(TestCase):
    def setUp(self):
        # self.obj = Questionario(
        #         nome='Samuel Barbosa',
        #         cpf='12345678901',
        #         sexo='M',
        #         cidade='Palmas',
        #         email='samuka1@gmail.com'
        # )
        self.obj = mommy.make(QuestionarioOld, nome='Samuel Barbosa', cpf='65673063008', _fill_optional=True)
        self.obj.save()


#     # @skipIf(AssertionError, "Salvar desabilitado na view")
    def test_create(self):
        self.assertTrue(QuestionarioOld.objects.exists())

    def test_criado_em(self):
        """Questionario deve conter campo para registro de quando foi criado"""
        self.assertIsInstance(self.obj.criado_em, datetime)

    # @skipIf(AssertionError, "utilizando mommy model")
    def test_str(self):
        self.assertEqual('Samuel Barbosa', str(self.obj))


class QuestionarioModelTest(TestCase):
    def setUp(self):
        # self.obj = Questionario(
        #         nome='Samuel Barbosa',
        #         cpf='12345678901',
        #         sexo='M',
        #         cidade='Palmas',
        #         email='samuka1@gmail.com'
        # )
        self.aluno = mommy.make(Aluno, nome='Samuel Barbosa', cpf='65673063008', _fill_optional=True)
        self.economica = mommy.make(DimensaoEconomica, _fill_optional=True)
        self.social = mommy.make(DimensaoSocial, _fill_optional=True)
        self.cultural = mommy.make(DimensaoCultural, _fill_optional=True)
        self.ambiental = mommy.make(DimensaoAmbiental, _fill_optional=True)
        self.obj = mommy.prepare(Questionario, aluno=self.aluno, economica=self.economica, cultural=self.cultural,
                                 ambiental=self.ambiental, social=self.social, _fill_optional=True)
        self.obj.aluno = self.aluno
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


