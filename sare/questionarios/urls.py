from django.conf.urls import url

from sare.questionarios.views import detalhe, new, consulta

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^([\w-]+)/$', detalhe, name='detalhe'),
    url(r'^consultar$', consulta, name='consulta'),
    # url(r'^([?P<cpf>\d+]/[<?P<matricula>\d+])/$', consulta, name='consulta'),
]
