from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template.loader import render_to_string

from sare.questionarios.forms import QuestionarioForm

from sare.questionarios.models import Questionario


def questionario(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):

    return render(request, 'questionarios/form_socioeconomico.html',
                  {'form': QuestionarioForm()})


def detalhe(request, pk):
    try:
        questionario = Questionario.objects.get(pk=pk)
    except Questionario.DoesNotExist:
        raise Http404

    # questionario = Questionario(
    #     nome='Samuel Barbosa',
    #     email='samuka1@gmail.com',
    #     cpf='12345678901',
    #     cidade='Palmas',
    # )
    return render(request, 'questionarios/detalhes.html',
                  {'quest':questionario})



def create(request):
    # Recebe os dados do formulário
    form = QuestionarioForm(request.POST)

    if not form.is_valid():
        return render(request, ['questionarios/form_socioeconomico.html', 'material/includes/material_css.html',
                                'material/includes/material_js.html', 'material/form.html'],
                      {'form': form})

    quest = Questionario.objects.create(**form.cleaned_data)

    _send_mail('Questionário Socioeconômico preenchido com sucesso',
               'pescar.gt.ss@gmail.com',
               quest.email,
               'questionarios/questionario_email.txt',
               {'quest': quest})

    return HttpResponseRedirect('/questionario/{}/'.format(quest.pk))


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)

    mail.send_mail(subject,
                   body,
                   from_,
                   [to])

