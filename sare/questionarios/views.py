import xlwt
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string, get_template
from django.views.generic import DetailView

from sare.core.views import busca
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


# def detalhe(request, hashid):
#     try:
#         questionario = Questionario.objects.get(hashId=hashid)
#     except Questionario.DoesNotExist:
#         raise Http404
#
#     return render(request, 'questionarios/detalhes.html',
#                   {'quest': questionario})

detalhe = DetailView.as_view(model=Questionario, template_name='questionarios/detalhes.html', slug_field='hashId')


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


@login_required(login_url='/admin/login/?next=/pytesexport/xls/')
def export_users_xls(request):



    response = HttpResponse(content_type='applications/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="inscricoes.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Questionários')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nome', 'Cpf', 'Curso']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Questionario.objects.all().values_list('nome', 'cpf', 'curso')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response