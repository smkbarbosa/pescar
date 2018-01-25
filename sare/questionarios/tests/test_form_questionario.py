from django.test import TestCase
from sare.questionarios.forms import QuestionarioForm
# from sare.questionarios.models import Questionario


class QuestionarioFormTest(TestCase):

    def setUp(self):
        self.form = QuestionarioForm()


    def test_form_has_fields(self):
        """Form deve conter campos """
        expected = ['nome', 'cpf', 'email',
                    'bairro',
                    'cidade',
                    'sexo',
                    # 'dependentes_RBD', 'origem_renda',
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
                    # 'pne_def_mental_grave', 'psico_dificuldade_concentrar', 'psico_conflito_familiar',
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
                    # 'forma_descarte_lixo', 'percepcao_seguranca_bairro',
                    # 'problemas_bairro',
                    # 'fale_mais_familia'
                    ]
        self.assertSequenceEqual(expected, list(self.form.fields))

