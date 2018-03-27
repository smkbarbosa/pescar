from django.conf.urls import url

from sare.questionarios import views
from sare.questionarios.views import detalhe, new, consulta


urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^(?P<slug>[\w-]+)/$', detalhe, name='detalhe'),
    # url(r'^(?P<pk>\d+)/$', detalhe, name='detalhe'),
    url(r'^consultar$', consulta, name='consulta'),
    # url(r'^([?P<cpf>\d+]/[<?P<matricula>\d+])/$', consulta, name='consulta'),
    url(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),
]
