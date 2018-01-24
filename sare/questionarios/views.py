from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from sare.questionarios.forms import QuestionarioForm


def questionario(request):
    if request.method == 'POST':
        return create(request)
    else :
        return new(request)


def create(request):
    # Recebe os dados do formulário
    form = QuestionarioForm(request.POST)

    if not form.is_valid():
        return render(request, ['questionarios/form_socioeconomico.html', 'material/includes/material_css.html',
                                'material/includes/material_js.html', 'material/form.html'],
                      {'form': form})

    _send_mail('Questionário Socioeconômico preenchido com sucesso',
               'pescar.gt.ss@gmail.com',
               form.cleaned_data['email'],
               'questionarios/questionario_email.txt',
               form.cleaned_data)

    messages.success(request, 'Questionário respondido com sucesso!')

    return HttpResponseRedirect('/questionario/')


def new(request):

    return render(request, 'questionarios/form_socioeconomico.html',
                  {'form': QuestionarioForm()})

def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)

    mail.send_mail(subject,
                   body,
                   from_,
                   [to])