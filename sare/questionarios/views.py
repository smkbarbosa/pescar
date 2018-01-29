from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from formtools.wizard.views import SessionWizardView

from sare.questionarios.forms import QuestionarioPessoalForm, QuestionarioEconomicoForm, QuestionarioCulturalForm, \
    QuestionarioAmbientalForm, QuestionarioFinalForm

# from sare.questionarios.models import Questionario


# def questionario(request):
#     if request.method == 'POST':
#         return create(request)
#     else :
#         return new(request)


# def create(request):
#     # Recebe os dados do formulário
#     form = QuestionarioWizard(request.POST)
#
#     if not form.is_valid():
#         return render(request, ['questionarios/form_socioeconomico.html', 'material/includes/material_css.html',
#                                 'material/includes/material_js.html', 'material/form.html'],
#                       {'form': form})
#
#     _send_mail('Questionário Socioeconômico preenchido com sucesso',
#                'pescar.gt.ss@gmail.com',
#                form.cleaned_data['email'],
#                'questionarios/questionario_email.txt',

#                form.cleaned_data)

    # Questionario.objects.create(**form.cleaned_data)

    # messages.success(request, 'Questionário respondido com sucesso!')
    #
    # return HttpResponseRedirect('/questionario/')


# def new(request):
#
#     return render(request, 'questionarios/form_socioeconomico.html',
#                   {'form': QuestionarioWizard()})


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)

    mail.send_mail(subject,
                   body,
                   from_,
                   [to])
#
#
# def show_message_form_condition(wizard):
#     # try to get the cleaned data of step 1
#     cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
#     # check if the field ``leave_message`` was checked.
#     return cleaned_data.get('leave_message', True)

class QuestionarioWizard(SessionWizardView):


    def show_message_form_condition(wizard):
        # try to get the cleaned data of step 1
        cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
        # check if the field ``leave_message`` was checked.
        return cleaned_data.get('leave_message', True)

    template_name = 'questionarios/form_socioeconomico.html'
    form_list = [
        QuestionarioPessoalForm,
        QuestionarioEconomicoForm,
        QuestionarioCulturalForm,
        QuestionarioAmbientalForm,
        QuestionarioFinalForm
    ]
    def done(self, form_list, **kwargs):
        return render(self.request, 'questionarios/form_final.html', {
            'form_data': [form.cleaned_data for form in form_list]
        })
