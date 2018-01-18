from django.http import HttpResponse
from django.shortcuts import render


def questionario(request):
    return render(request, 'questionarios/form_socioeconomico.html')