from django.shortcuts import render
from sare.questionarios.forms import QuestionarioForm


def questionario(request):
    context = {'form': QuestionarioForm() }
    return render(request, 'questionarios/form_socioeconomico.html', context)