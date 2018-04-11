import xlwt
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string, get_template

from sare.questionarios.forms import QuestionarioForm
from sare.questionarios.models import Questionario


def new(request):
    if request.method == 'POST':
    #     return HttpResponseRedirect(r(busca))
    # return HttpResponseRedirect(r(busca))
        return create(request)
    return empty_form(request)


def empty_form(request):
    return render(request, 'questionarios/form_socioeconomico.html',
                  {'form': QuestionarioForm()})


def detalhe(request, hashid):
    try:
        questionario = Questionario.objects.get(hashId=hashid)
    except Questionario.DoesNotExist:
        raise Http404

    return render(request, 'questionarios/detalhes.html',
                  {'quest': questionario})

# detalhe = DetailView.as_view(model=Questionario, template_name='questionarios/detalhes.html', slug_field='hashId')


def consulta(request):

    # if request.method == 'POST':
        # import ipdb
        #
        # ipdb.set_trace()
        # form = BuscaForm(request.POST)
        # if not form.is_valid():
        #     return render(request, r('busca'),
        #                   {'form': form})

    cpf = request.POST['cpf']
    matricula = request.POST['matricula']

    c = Questionario.objects.filter(cpf=cpf, matricula=matricula).first()
    if c is None:
        raise Http404
    return HttpResponseRedirect(r('questionarios:detalhe', c.hashId))


def create(request):
    # Recebe os dados do formulário
    form = QuestionarioForm(request.POST)

    # import ipdb
    #
    # ipdb.set_trace()
    if not form.is_valid():
        return render(request, 'questionarios/form_socioeconomico.html',
                      {'form': form})

    quest = form.save()

    _send_mail('Questionário Socioeconômico preenchido com sucesso',
               'clae.palmas@ifto.edu.br',
               quest.email,
               'questionarios/questionario_email.txt',
               {'quest': quest}
               )

    return HttpResponseRedirect(r('questionarios:detalhe', quest.hashId))


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    template_html = 'questionarios/detalhes-email.html'
    html = get_template(template_html)
    html_content = html.render(context)

    # mail.send_mail(subject,
    #                body,
    #                from_,
    #                [to],
    #                html_message=msg_html,
    #                )

    msg = EmailMultiAlternatives(subject, body, from_, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@login_required(login_url='/admin/login/?next=/export/xls/')
def export_users_xls(request):

    response = HttpResponse(content_type='applications/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="inscricoes.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Questionários')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['NOME', 'CPF',
               'EMAIL', 'SEXO', 'FONE',
               'ENDERECO', 'NUM_CASA', 'CEP', 'BAIRRO',
               'CIDADE', 'ESTADO',
               'CURSO', 'SEMESTRE/ANO', 'MATRICULA', 'CAMPUS',
               'DEPENDENTES DA RENDA', 'ORIGEM DA RENDA',
               'RENDA BRUTA DOMICILIAR',
               'RESPONSAVEL DOMICILIO', 'RENDA PER CAPITA', 'RELACAO FINANCEIRA',
               'DESPESAS_SAUDE_TRATAMENTO', 'DESPESAS_SAUDE_MEDICAMENTO', 'DESPESAS_SAUDE_CUIDADOR',
               'DESPESAS_SAUDE_PLANO', 'DESPESAS_TRANSPORTE', 'DESPESAS_MORADIA',
               'DESPESAS_EDUCACAO_SUPERIOR', 'DESPESAS_EDUCACAO_BASICO', 'DESPESAS_EDUCACAO_CURSINHO',
               'DESPESAS_EDUCACAO_CAPACITACAO', 'DESPESAS_EDUCACAO_MATERIAL', 'DESPESAS_BENS_FCARRO',
               'DESPESAS_BENS_FMOTO', 'DESPESAS_BENS_TERRENO', 'DESPESAS_DOMESTICAS_ELETRICA',
               'DESPESAS_DOMESTICAS_AGUA', 'DESPESAS_DOMESTICAS_ALIMENTACAO',
               'CONDICAO_RESPONSAVEL_CASA', 'MEIO_ACESSO_CAMPUS', 'CONDICAO_MORADIA', 'LOCAL_MORADIA',
               'TOTAL_PESSOAS_CASA', 'TOTAL_COMODOS_CASA', 'TOTAL_KM_CASA_CAMPUS',
               'INSTITUICAO_ANTERIOR',
               'SAUDE_BEBIDA_DROGAS', 'SAUDE_DOENCA_GRAVE', 'SAUDE_DOENCA_CRONICA',
               'SAUDE_MEDICAMENTO_DIARIO',
               'PNE_PARCIAL_VISAO_AUDICAO', 'PNE_DEF_FISICA', 'PNE_TOTAL_VISAO_AUDICAO',
               'PNE_DEF_MENTAL_LEVE',
               'PNE_DEF_MENTAL_GRAVE', 'PSICO_DIFICULDADE_CONCENTRAR', 'PSICO_CONFLITO_FAMILIAR',
               'PSICO_DEPRESSAO',
               'COR_RACA', 'VIOLENCIA_VERBAL', 'VIOLENCIA_URBANA', 'VIOLENCIA_PATRIMONIAL',
               'VIOLENCIA_CYBERBULLING', 'VIOLENCIA_RELIGIOSA', 'VIOLENCIA_ASSEDIO_MORAL',
               'VIOLENCIA_ABANDONO',
               'VIOLENCIA_ABUSO_FAMILIAR', 'VIOLENCIA_ATENTADO_PUDOR', 'VIOLENCIA_TRAFICO_HUMANO',
               'VIOLENCIA_PSICOLOGICA_MORAL', 'VIOLENCIA_FISICA', 'VIOLENCIA_SEXUAL',
               'PRECONCEITO_CULTURAL',
               'PRECONCEITO_ESTETICO', 'PRECONCEITO_ECONOMICO', 'PRECONCEITO_RELIGIOSO',
               'PRECONCEITO_MENTAL',
               'PRECONCEITO_RACIAL', 'PRECONCEITO_GENERO', 'PRECONCEITO_ORIENTACAO_SEXUAL',
               'FORMA_DESCARTE_LIXO', 'PERCEPCAO_SEGURANCA_BAIRRO',
               'FALE_MAIS_FAMILIA',
               ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    # Nessa linha, o curso é gerado com o numero ao inves do nome, pra resolver a treta, usamos list comprehensions
    # rows = Questionario.objects.all().values_list('nome', 'cpf',
    #                                               'email', 'sexo', 'fone',
    #                                               'endereco', 'num_casa', 'cep', 'bairro',
    #                                               'cidade', 'estado',
    #                                               'curso', 'sem_mod_ano', 'matricula', 'campus',
    #                                               'dependentes_RBD', 'origem_renda',
    #                                               'renda_bruta_domiciliar',
    #                                               'responsavel_domicilio', 'renda_per_capita', 'relacao_financeira',
    #                                               'despesas_saude_tratamento', 'despesas_saude_medicamento', 'despesas_saude_cuidador',
    #                                               'despesas_saude_plano', 'despesas_transporte', 'despesas_moradia',
    #                                               'despesas_educacao_superior', 'despesas_educacao_basico', 'despesas_educacao_cursinho',
    #                                               'despesas_educacao_capacitacao', 'despesas_educacao_material', 'despesas_bens_fcarro',
    #                                               'despesas_bens_fmoto', 'despesas_bens_terreno', 'despesas_domesticas_eletrica',
    #                                               'despesas_domesticas_agua', 'despesas_domesticas_alimentacao',
    #                                               'condicao_responsavel_casa', 'meio_acesso_campus', 'condicao_moradia', 'local_moradia',
    #                                               'total_pessoas_casa', 'total_comodos_casa', 'total_km_casa_campus',
    #                                               'instituicao_anterior',
    #                                               'saude_bebida_drogas', 'saude_doenca_grave', 'saude_doenca_cronica',
    #                                               'saude_medicamento_diario',
    #                                               'pne_parcial_visao_audicao', 'pne_def_fisica', 'pne_total_visao_audicao',
    #                                               'pne_def_mental_leve',
    #                                               'pne_def_mental_grave', 'psico_dificuldade_concentrar', 'psico_conflito_familiar',
    #                                               'psico_depressao',
    #                                               'cor_raca', 'violencia_verbal', 'violencia_urbana', 'violencia_patrimonial',
    #                                               'violencia_cyberbulling', 'violencia_religiosa', 'violencia_assedio_moral',
    #                                               'violencia_abandono',
    #                                               'violencia_abuso_familiar', 'violencia_atentado_pudor', 'violencia_trafico_humano',
    #                                               'violencia_psicologica_moral', 'violencia_fisica', 'violencia_sexual',
    #                                               'preconceito_cultural',
    #                                               'preconceito_estetico', 'preconceito_economico', 'preconceito_religioso',
    #                                               'preconceito_mental',
    #                                               'preconceito_racial', 'preconceito_genero', 'preconceito_orientacao_sexual',
    #                                               'forma_descarte_lixo', 'percepcao_seguranca_bairro',
    #                                               'fale_mais_familia',)
    rows = [(q.nome, q.cpf, q.email, q.sexo, q.fone, q.endereco, q.num_casa, q.cep, q.bairro, q.cidade, q.estado,
             q.get_curso_display(), q.sem_mod_ano, q.matricula, q.campus, q.dependentes_RBD, q.origem_renda,
             q.renda_bruta_domiciliar, q.responsavel_domicilio, q.renda_per_capita, q.relacao_financeira,
             q.despesas_saude_tratamento, q.despesas_saude_medicamento, q.despesas_saude_cuidador,
             q.despesas_saude_plano, q.despesas_transporte, q.despesas_moradia, q.despesas_educacao_superior,
             q.despesas_educacao_basico, q.despesas_educacao_cursinho, q.despesas_educacao_capacitacao,
             q.despesas_educacao_material, q.despesas_bens_fcarro, q.despesas_bens_fmoto, q.despesas_bens_terreno,
             q.despesas_domesticas_eletrica, q.despesas_domesticas_agua, q.despesas_domesticas_alimentacao,
             q.get_condicao_responsavel_casa_display(), q.get_meio_acesso_campus_display(),
             q.get_condicao_moradia_display(), q.get_local_moradia_display(), q.get_total_pessoas_casa_display(),
             q.get_total_comodos_casa_display(), q.get_total_km_casa_campus_display(),
             q.get_instituicao_anterior_display(), q.get_saude_bebida_drogas_display(),
             q.get_saude_doenca_grave_display(), q.get_saude_doenca_cronica_display(),
             q.get_saude_medicamento_diario_display(), q.get_pne_parcial_visao_audicao_display(),
             q.get_pne_def_fisica_display(), q.get_pne_total_visao_audicao_display(),
             q.get_pne_def_mental_leve_display(), q.get_pne_def_mental_grave_display(),
             q.get_psico_dificuldade_concentrar_display(), q.get_psico_conflito_familiar_display(),
             q.get_psico_depressao_display(), q.get_cor_raca_display(), q.get_violencia_verbal_display(),
             q.get_violencia_urbana_display(), q.get_violencia_patrimonial_display(),
             q.get_violencia_cyberbulling_display(), q.get_violencia_religiosa_display(),
             q.get_violencia_assedio_moral_display(), q.get_violencia_abandono_display(),
             q.get_violencia_abuso_familiar_display(), q.get_violencia_atentado_pudor_display(),
             q.get_violencia_trafico_humano_display(), q.get_violencia_psicologica_moral_display(),
             q.get_violencia_fisica_display(), q.get_violencia_sexual_display(), q.get_preconceito_cultural_display(),
             q.get_preconceito_estetico_display(), q.get_preconceito_economico_display(),
             q.get_preconceito_religioso_display(), q.get_preconceito_mental_display(),
             q.get_preconceito_racial_display(), q.get_preconceito_genero_display(),
             q.get_preconceito_orientacao_sexual_display(), q.get_forma_descarte_lixo_display(),
             q.get_percepcao_seguranca_bairro_display(), q.fale_mais_familia) for q in Questionario.objects.all()]

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
