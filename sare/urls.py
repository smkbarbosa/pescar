from django.conf.urls import url, include
from django.contrib import admin
import debug_toolbar
from sare.core.views import HomeView, busca
import debug_toolbar

urlpatterns = [
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^consultar$', busca, name='busca'),
    url(r'^questionario/', include('sare.questionarios.urls',
                                   namespace='questionarios')),
    url(r'^entrevista/', include('sare.entrevista.urls',
                                   namespace='entrevista')),
    url(r'^admin/', admin.site.urls),
    url(r'^__debug__/', include(debug_toolbar.urls)),
]
