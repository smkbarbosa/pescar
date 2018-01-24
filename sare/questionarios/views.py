from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from sare.questionarios.forms import QuestionarioForm


def questionario(request):
    if request.method == 'POST':

        # Recebe os dados do formulário
        form = QuestionarioForm(request.POST)

        if form.is_valid():

            body = render_to_string('questionarios/questionario_email.txt', form.cleaned_data)

            mail.send_mail('Questionário Socioeconômico preenchido com sucesso',
                           body,
                           'pescar.gt.ss@gmail.com',
                           [form.cleaned_data['email']])

            messages.success(request, 'Questionário respondido com sucesso!')

            return HttpResponseRedirect('/questionario/')

        else:
            return render(request, ['questionarios/form_socioeconomico.html','material/includes/material_css.html', 'material/includes/material_js.html', 'material/form.html'],
                          {'form': form})



    else:
        context = {'form': QuestionarioForm() }
        return render(request, 'questionarios/form_socioeconomico.html', context)

