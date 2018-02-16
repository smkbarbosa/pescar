from django.conf.urls import url

from sare.questionarios.views import detalhe, new

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^([\w-]+)/$', detalhe, name='detalhe'),
]