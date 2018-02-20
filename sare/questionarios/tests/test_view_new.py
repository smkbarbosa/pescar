from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r
from model_mommy import mommy

from sare.questionarios.forms import QuestionarioForm
from sare.questionarios.models import Questionario


class QuestionarioNovoGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('questionarios:new'))

    def test_get(self):
        """GET /questionario/ deve retornar status code 200"""
        self.assertEqual(200, self.resp.status_code)

    # def test_template(self):
    #     """Deve utilizar o template form_socioeconomico.html"""
    #     self.assertTemplateUsed(self.resp, 'questionarios/form_socioeconomico.html')

    def test_html(self):
        """HTML deve conter algumas tags específicas"""
        tags = (('<form', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """Html deve conter csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


    def test_has_form(self):
        """Context deve ter form de questionario"""
        form = self.resp.context['form']
        self.assertIsInstance(form, QuestionarioForm)


class QuestionarioNovoPost(TestCase):
    def setUp(self):
        # self.data = {'nome': 'Samuel Barbosa',
        #         'cpf': '12345678901',
        #         'email': 'samuka1@gmail.com',
        #         'cidade': 'Palmas',
        #         'sexo': 'M',
        #         'dependentes_RBD': '2',
        #         'origem_renda': '1',
        #         'renda_bruta_domiciliar': '1',
        #         'responsavel_domicilio': 'jovem', 'renda_per_capita': '1', 'relacao_financeira': '1',
        #         'despesas_saude_tratamento': '1', 'despesas_saude_medicamento': '1', 'despesas_saude_cuidador': '1',
        #         'despesas_saude_plano': '1', 'despesas_transporte': '1', 'despesas_moradia': '1',
        #         'despesas_educacao_superior': '1', 'despesas_educacao_basico': '1', 'despesas_educacao_cursinho': '0',
        #         'despesas_educacao_capacitacao': '0', 'despesas_educacao_material': '0', 'despesas_bens_fcarro': '0',
        #         'despesas_bens_fmoto': '0', 'despesas_bens_terreno': '0', 'despesas_domesticas_eletrica': '0',
        #         'despesas_domesticas_agua': '0', 'despesas_domesticas_alimentacao': '0',
        #         'condicao_responsavel_casa': '1', 'meio_acesso_campus': '1', 'condicao_moradia': '1',
        #         'local_moradia': '1',
        #         'total_pessoas_casa': '1', 'total_comodos_casa': '1', 'total_km_casa_campus': '1',
        #         'instituicao_anterior': '1',
        #         'saude_bebida_drogas': '1', 'saude_doenca_grave': '1', 'saude_doenca_cronica': '1',
        #         'saude_medicamento_diario': '1',
        #         'pne_parcial_visao_audicao': '1', 'pne_def_fisica': '1', 'pne_total_visao_audicao': '1',
        #         'pne_def_mental_leve': '1',
        #         'pne_def_mental_grave': '1', 'psico_dificuldade_concentrar': '1', 'psico_conflito_familiar': '1',
        #         'psico_depressao': '1',
        #         'cor_raca': '1', 'violencia_verbal': '1', 'violencia_urbana': '1', 'violencia_patrimonial': '1',
        #         'violencia_cyberbulling': '1', 'violencia_religiosa': '1', 'violencia_assedio_moral': '1',
        #         'violencia_abandono': '1',
        #         'violencia_abuso_familiar': '1', 'violencia_atentado_pudor': '1', 'violencia_trafico_humano': '1',
        #         'violencia_psicologica_moral': '1', 'violencia_fisica': '1', 'violencia_sexual': '1',
        #         'preconceito_cultural': '1',
        #         'preconceito_estetico': '1', 'preconceito_economico': '1', 'preconceito_religioso': '1',
        #         'preconceito_mental': '1',
        #         'preconceito_racial': '1', 'preconceito_genero': '1', 'preconceito_orientacao_sexual': '1',
        #         'servicos_indisponiveis_bairro': '1',
        #         'forma_descarte_lixo': '1', 'percepcao_seguranca_bairro': '1',
        #         'problemas_bairro': '1', 'fale_mais_familia': 'ok'
        # }

        self.obj = mommy.make(Questionario, cpf='12345678901', email='samuka1@gmail.com', _fill_optional=True)
        # self.obj = mommy.prepare_recipe('sare.questionarios.quest', _fill_optional=True, _save_related=True)
        form_fields = ['hashId', 'criado_em', 'nome', 'cpf', 'email',
                       'bairro',
                       'cidade',
                       'sexo',
                       'dependentes_RBD', 'origem_renda',
                       'renda_bruta_domiciliar',
                       'responsavel_domicilio', 'renda_per_capita', 'relacao_financeira',
                       'despesas_saude_tratamento', 'despesas_saude_medicamento', 'despesas_saude_cuidador',
                       'despesas_saude_plano', 'despesas_transporte', 'despesas_moradia',
                       'despesas_educacao_superior', 'despesas_educacao_basico', 'despesas_educacao_cursinho',
                       'despesas_educacao_capacitacao', 'despesas_educacao_material', 'despesas_bens_fcarro',
                       'despesas_bens_fmoto', 'despesas_bens_terreno', 'despesas_domesticas_eletrica',
                       'despesas_domesticas_agua', 'despesas_domesticas_alimentacao',
                       'condicao_responsavel_casa', 'meio_acesso_campus', 'condicao_moradia', 'local_moradia',
                       'total_pessoas_casa', 'total_comodos_casa', 'total_km_casa_campus',
                       'instituicao_anterior',
                       'saude_bebida_drogas', 'saude_doenca_grave', 'saude_doenca_cronica',
                       'saude_medicamento_diario',
                       'pne_parcial_visao_audicao', 'pne_def_fisica', 'pne_total_visao_audicao',
                       'pne_def_mental_leve',
                       'pne_def_mental_grave', 'psico_dificuldade_concentrar', 'psico_conflito_familiar',
                       'psico_depressao',
                       'cor_raca', 'violencia_verbal', 'violencia_urbana', 'violencia_patrimonial',
                       'violencia_cyberbulling', 'violencia_religiosa', 'violencia_assedio_moral',
                       'violencia_abandono',
                       'violencia_abuso_familiar', 'violencia_atentado_pudor', 'violencia_trafico_humano',
                       'violencia_psicologica_moral', 'violencia_fisica', 'violencia_sexual',
                       'preconceito_cultural',
                       'preconceito_estetico', 'preconceito_economico', 'preconceito_religioso',
                       'preconceito_mental',
                       'preconceito_racial', 'preconceito_genero', 'preconceito_orientacao_sexual',
                       'servicos_indisponiveis_bairro',
                       'forma_descarte_lixo', 'percepcao_seguranca_bairro',
                       'problemas_bairro', 'fale_mais_familia'
                       ]
        self.data = {field: getattr(self.obj, field) for field in form_fields}

        self.resp = self.client.post(r('questionarios:new'), self.data)
        self.id = Questionario.objects.first().hashId
        self.email = mail.outbox[0]

    def test_post(self):
        """POST valid deve redirecionar to /questionario/1/"""
        self.assertRedirects(self.resp, r('questionarios:detalhe', self.id))

    def test_envia_email_questionario(self):
        self.assertEqual(1, len(mail.outbox))

#
#     # @skipIf(AssertionError, "Salvar desabilitado na view")
    def test_salva_questionario(self):
        self.assertTrue(Questionario.objects.exists())


class QuestionarioNovoPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('questionarios:new'), {})  # data é um dicionário vazio

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

    def test_nao_salva_questionario(self):
        self.assertFalse(Questionario.objects.exists())

# from unittest import skipIf
#
# from django.core import mail
# from django.test import TestCase
# from django.shortcuts import resolve_url as r
# from model_mommy import mommy
#
# from sare.questionarios.forms import QuestionarioForm
# from sare.questionarios.models import Questionario
#
#
# class QuestionarioNovoGet(TestCase):
#     def setUp(self):
#         self.resp = self.client.get(r('questionarios:new'))
#
#     def test_get(self):
#         """GET /questionario/ deve retornar status code 200"""
#         self.assertEqual(200, self.resp.status_code)
#
#     # def test_template(self):
#     #     """Deve utilizar o template form_socioeconomico.html"""
#     #     self.assertTemplateUsed(self.resp, 'questionarios/form_socioeconomico.html')
#
#     def test_html(self):
#         """HTML deve conter algumas tags específicas"""
#         tags = (('<form', 1),
#                 ('type="submit"', 1))
#
#         for text, count in tags:
#             with self.subTest():
#                 self.assertContains(self.resp, text, count)
#
#     def test_csrf(self):
#         """Html deve conter csrf"""
#         self.assertContains(self.resp, 'csrfmiddlewaretoken')
#
#
#     def test_has_form(self):
#         """Context deve ter form de questionario"""
#         form = self.resp.context['form']
#         self.assertIsInstance(form, QuestionarioForm)


# class QuestionarioNovoPost(TestCase):
#     def setUp(self):
#         # data = {'nome':'Samuel Barbosa',
#         #         'cpf':'12345678901',
#         #         'email':'samuka1@gmail.com',
#         #         'cidade':'Palmas',
#         #         'condicao_responsavel_casa':'1',
#         #         'meio_acesso_campus':'1',
#         #         'condicao_moradia':'5',
#         #         'local_moradia':'1',
#         #         'total_pessoas_casa':'2',
#         #         'total_comodos_casa':'3',
#         #         'total_km_casa_campus':'2',
#         #         'instituicao_anterior':'6'
#         # }
#
#         self.obj = mommy.make(Questionario, nome='Samuel Barbosa', cpf='12345678901')
#         form_fields = ['nome', 'cpf', 'email',
#                        'bairro',
#                        'cidade',
#                        'sexo',
#                        'dependentes_RBD', 'origem_renda',
#                        'renda_bruta_domiciliar',
#                        'responsavel_domicilio', 'renda_per_capita', 'relacao_financeira',
#                        'despesas_saude_tratamento', 'despesas_saude_medicamento', 'despesas_saude_cuidador',
#                        'despesas_saude_plano', 'despesas_transporte', 'despesas_moradia',
#                        'despesas_educacao_superior', 'despesas_educacao_basico', 'despesas_educacao_cursinho',
#                        'despesas_educacao_capacitacao', 'despesas_educacao_material', 'despesas_bens_fcarro',
#                        'despesas_bens_fmoto', 'despesas_bens_terreno', 'despesas_domesticas_eletrica',
#                        'despesas_domesticas_agua', 'despesas_domesticas_alimentacao',
#                        'condicao_responsavel_casa', 'meio_acesso_campus', 'condicao_moradia', 'local_moradia',
#                        'total_pessoas_casa', 'total_comodos_casa', 'total_km_casa_campus',
#                        'instituicao_anterior',
#                        'saude_bebida_drogas', 'saude_doenca_grave', 'saude_doenca_cronica',
#                        'saude_medicamento_diario',
#                        'pne_parcial_visao_audicao', 'pne_def_fisica', 'pne_total_visao_audicao',
#                        'pne_def_mental_leve',
#                        'pne_def_mental_grave', 'psico_dificuldade_concentrar', 'psico_conflito_familiar',
#                        'psico_depressao',
#                        'cor_raca', 'violencia_verbal', 'violencia_urbana', 'violencia_patrimonial',
#                        'violencia_cyberbulling', 'violencia_religiosa', 'violencia_assedio_moral',
#                        'violencia_abandono',
#                        'violencia_abuso_familiar', 'violencia_atentado_pudor', 'violencia_trafico_humano',
#                        'violencia_psicologica_moral', 'violencia_fisica', 'violencia_sexual',
#                        'preconceito_cultural',
#                        'preconceito_estetico', 'preconceito_economico', 'preconceito_religioso',
#                        'preconceito_mental',
#                        'preconceito_racial', 'preconceito_genero', 'preconceito_orientacao_sexual',
#                        'servicos_indisponiveis_bairro',
#                        'forma_descarte_lixo', 'percepcao_seguranca_bairro',
#                        'problemas_bairro', 'fale_mais_familia', 'hashId', 'criado_em'
#                        ]
#         data = {field: getattr(self.obj, field) for field in form_fields}
#
#         self.resp = self.client.post(r('questionarios:new'), data)
#         self.id = Questionario.objects.first().hashId  # agregado
#
#         self.email = mail.outbox[0]
#
#     def test_post(self):
#         """POST valid deve redirecionar to /questionario/uuid/"""
#         self.assertRedirects(self.resp, r('questionarios:detalhe', self.id))
#
#     # @skipIf(AssertionError, 'descobrir')
#     def test_envia_email_questionario(self):
#         self.assertEqual(1, len(mail.outbox))
#
#     # @skipIf(AssertionError, "Salvar desabilitado na view")
#     def test_salva_questionario(self):
#         self.assertTrue(Questionario.objects.exists())
#         # self.assertTrue(Questionario.save(self.obj))
#
#
# class QuestionarioNovoPostInvalid(TestCase):
#     def setUp(self):
#         self.resp = self.client.post(r('questionarios:new'), {})  # data é um dicionário vazio
#
#     def test_post(self):
#         """Post Invalid não deve redirecionar"""
#         self.assertEqual(200, self.resp.status_code)
#
#     def test_template(self):
#         self.assertTemplateUsed(self.resp, 'questionarios/form_socioeconomico.html')
#         self.assertTemplateUsed(self.resp, 'material/includes/material_css.html')
#         self.assertTemplateUsed(self.resp, 'material/includes/material_js.html')
#         self.assertTemplateUsed(self.resp, 'material/form.html')
#
#     def test_has_form(self):
#         form = self.resp.context['form']
#         self.assertIsInstance(form, QuestionarioForm)
#
#     def test_form_has_errors(self):
#         form = self.resp.context['form']
#         self.assertTrue(form.errors)
#
#     def test_nao_salva_questionario(self):
#         self.assertFalse(Questionario.objects.exists())