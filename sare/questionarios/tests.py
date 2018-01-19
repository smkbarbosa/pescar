from django.test import TestCase
from  sare.questionarios.forms import QuestionarioForm


class QuestionarioTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/questionario/')

    def test_get(self):
        """GET /questionario/ deve retornar status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Deve usar questionario/form_socioeconomico.html"""
        self.assertTemplateUsed(self.resp, 'questionarios/form_socioeconomico.html')

    def test_html(self):
        """Html deve conter input tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<fieldset', 53 )
        self.assertContains(self.resp, '<legend', 52)
        self.assertContains(self.resp, '<p', 6)
        self.assertContains(self.resp, '<div', 153)
        self.assertContains(self.resp, '<input', 256)
        self.assertContains(self.resp, '<label', 225)
        self.assertContains(self.resp, 'type="text"', 26)
        self.assertContains(self.resp, 'type="checkbox"', 18)
        self.assertContains(self.resp, 'type="radio"', 207)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """Html deve conter csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context deve ter form de questionario"""
        form = self.resp.context['form']
        self.assertIsInstance(form, QuestionarioForm)

    def test_form_has_fields(self):
        """Form deve conter campos --- dimensão economica """
        form = self.resp.context['form']
        self.assertSequenceEqual(['nome', 'cpf', 'sexo', 'dependentes_RBD', 'origem_renda', 'renda_bruta_domiciliar',
                                  'responsavel_domicilio', 'renda_per_capita', 'relacao_financeira',
                                  'despesas_saude_tratamento', 'despesas_saude_medicamento', 'despesas_saude_cuidador',
                                  'despesas_saude_plano', 'despesas_transporte', 'despesas_moradia',
                                  'despesas_educacao_superior', 'despesas_educacao_basico', 'despesas_educacao_cursinho',
                                  'despesas_educacao_capacitacao', 'despesas_educacao_material', 'despesas_bens_fcarro',
                                  'despesas_bens_fmoto', 'despesas_bens_terreno', 'despesas_domesticas_eletrica',
                                  'despesas_domesticas_agua', 'despesas_domesticas_alimentacao',
                                  'condicao_responsavel_casa', 'meio_acesso_campus', 'condicao_moradia', 'local_moradia',
                                  'total_pessoas_casa', 'total_comodos_casa', 'total_km_casa_campus'
                                  ], list(form.fields))

