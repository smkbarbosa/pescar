from django.core import mail
from django.test import TestCase
from sare.questionarios.forms import QuestionarioForm
from sare.questionarios.models import Questionario


class QuestionarioFormTest(TestCase):

    def setUp(self):
        self.form = QuestionarioForm()

    def test_form_has_fields(self):
        """Form deve conter campos --- dimensão economica """
        expected = ['nome', 'cpf', 'email',
                    # 'bairro',
                    'cidade',
                    # 'sexo', 'dependentes_RBD', 'origem_renda',
                    # 'renda_bruta_domiciliar',
                    # 'responsavel_domicilio', 'renda_per_capita', 'relacao_financeira',
                    # 'despesas_saude_tratamento', 'despesas_saude_medicamento', 'despesas_saude_cuidador',
                    # 'despesas_saude_plano', 'despesas_transporte', 'despesas_moradia',
                    # 'despesas_educacao_superior', 'despesas_educacao_basico', 'despesas_educacao_cursinho',
                    # 'despesas_educacao_capacitacao', 'despesas_educacao_material', 'despesas_bens_fcarro',
                    # 'despesas_bens_fmoto', 'despesas_bens_terreno', 'despesas_domesticas_eletrica',
                    # 'despesas_domesticas_agua', 'despesas_domesticas_alimentacao',
                    # 'condicao_responsavel_casa', 'meio_acesso_campus', 'condicao_moradia', 'local_moradia',
                    # 'total_pessoas_casa', 'total_comodos_casa', 'total_km_casa_campus',
                    # 'instituicao_anterior',
                    # 'saude_bebida_drogas', 'saude_doenca_grave', 'saude_doenca_cronica',
                    # 'saude_medicamento_diario',
                    # 'pne_parcial_visao_audicao', 'pne_def_fisica', 'pne_total_visao_audicao',
                    # 'pne_def_mental_leve',
                    # 'pne_def_mental_grave', 'psico_dificudade_concentrar', 'psico_conflito_familiar',
                    # 'psico_depressao',
                    # 'cor_raca', 'violencia_verbal', 'violencia_urbana', 'violencia_patrimonial',
                    # 'violencia_cyberbulling', 'violencia_religiosa', 'violencia_assedio_moral',
                    # 'violencia_abandono',
                    # 'violencia_abuso_familiar', 'violencia_atentado_pudor', 'violencia_trafico_humano',
                    # 'violencia_psicologica_moral', 'violencia_fisica', 'violencia_sexual',
                    # 'preconceito_cultural',
                    # 'preconceito_estetico', 'preconceito_economico', 'preconceito_religioso',
                    # 'preconceito_mental',
                    # 'preconceito_racial', 'preconceito_genero', 'preconceito_orientacao_sexual',
                    # 'servicos_indisponiveis_bairro',
                    # 'forma_descarte_lixo', 'percepcao_seguranca_bairro', 'problemas_bairro',
                    # 'fale_mais_familia'
                    ]
        self.assertSequenceEqual(expected, list(self.form.fields))

class QuestionarioPostTest(TestCase):
    def setUp(self):
        data = dict(nome='Samuel Barbosa', cpf='12345678901',
                    email='samuka1@gmail.com',
                    cidade='Palmas')
        self.resp = self.client.post('/questionario/', data)

    def test_post(self):
        """POST valid deve redirecionar to /questionario/"""
        self.assertEqual(302, self.resp.status_code)

    def test_envia_email_questionario(self):
        self.assertEqual(1, len(mail.outbox))

    def test_email_questionario_assunto(self):
        email = mail.outbox[0]
        expect = 'Questionário Socioeconômico preenchido com sucesso'

        self.assertEqual(expect, email.subject)

    def test_email_questionario_remetente(self):
        email = mail.outbox[0]
        expect = 'pescar.gt.ss@gmail.com'

        self.assertEqual(expect, email.from_email)

    def test_email_questionario_para(self):
        email = mail.outbox[0]
        expect = ['samuka1@gmail.com',]

        self.assertEqual(expect, email.to)

    def test_questionario_corpo_email(self):
        email = mail.outbox[0]

        self.assertIn('Samuel Barbosa', email.body)
        self.assertIn('samuka1@gmail.com', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('Palmas', email.body)


    # def test_salva_questionario(self):
    #    self.assertTrue(Questionario.objects.exists())
    #   pass


class QuestionarioPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/questionario/', {}) # data é um dicionário vazio

    def test_post(self):
        """Post Invalid não deve redirecionar"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'questionarios/form_socioeconomico.html')
        self.assertTemplateUsed(self.resp, 'material/includes/material_css.html')
        self.assertTemplateUsed(self.resp, 'material/includes/material_js.html')
        self.assertTemplateUsed(self.resp, 'material/form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, QuestionarioForm)


    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    # def test_nao_salva_questionario(self):
    #    self.assertFalse(Questionario.objects.exists())
    #    pass

class QuestionarioSucessMessage(TestCase):
    def test_message(self):
        data = dict(nome='Samuel Barbosa', cpf='12345678901',
                    email='samuka1@gmail.com',
                    cidade='Palmas')

        response = self.client.post('/questionario/', data, follow=True)
        self.assertContains(response, 'Questionário respondido com sucesso!')