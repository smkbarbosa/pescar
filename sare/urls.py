from django.conf.urls import url, include
from django.contrib import admin

from sare.core.views import HomeView, BuscaView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^consultar$', BuscaView.as_view(), name='busca'),
    url(r'^questionario/', include('sare.questionarios.urls',
                                   namespace='questionarios')),
    url(r'^admin/', admin.site.urls),
]