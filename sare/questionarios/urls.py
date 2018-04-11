from django.conf.urls import url

from sare.core.forms import AlunoForm
from sare.questionarios import views
from sare.questionarios.forms import QuestionarioForm
from sare.questionarios.views import detalhe, new, consulta, QuestionarioView


urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^form/$', QuestionarioView.as_view([AlunoForm, QuestionarioForm])),
    # url(r'^(?P<slug>[\w-]+)/$', detalhe, name='detalhe'),
    url(r'^([\w-]+)/$', detalhe, name='detalhe'),
    # url(r'^(?P<pk>\d+)/$', detalhe, name='detalhe'),
    url(r'^consultar$', consulta, name='consulta'),
    # url(r'^([?P<cpf>\d+]/[<?P<matricula>\d+])/$', consulta, name='consulta'),
    url(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),
]
