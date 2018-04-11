from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import MultipleObjectMixin

from sare.questionarios.forms import BuscaForm


class GenericHomeView(MultipleObjectMixin, TemplateView):
    pass

class HomeView(GenericHomeView):
    template_name = 'index.html'
    object_list = None


class BuscaView(GenericHomeView):
    template_name = 'consulta.html'
    form = BuscaForm()
    object_list = None

    def get(self, *args, **kwargs):
        return self.render_to_response({'form': self.form})

    def render_to_response(self, context):
        return render(self.request, self.template_name, context)

# def busca(request):
#     form = BuscaForm()
#     return render(request, 'consulta.html', {'form':form})