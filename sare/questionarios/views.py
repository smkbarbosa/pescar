import datetime
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string, get_template

from sare.core.views import busca
from sare.questionarios.forms import QuestionarioForm, BuscaForm
from sare.questionarios.models import QuestionarioOld


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
        questionario = QuestionarioOld.objects.get(hashId=hashid)
    except QuestionarioOld.DoesNotExist:
        raise Http404

    return render(request, 'questionarios/detalhes.html',
                  {'quest': questionario})


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

    c = QuestionarioOld.objects.filter(cpf=cpf, matricula=matricula).first()
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

    return HttpResponseRedirect(r('questionarios:detalhe', str(quest.hashId)))


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

