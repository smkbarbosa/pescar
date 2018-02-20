from django.conf.urls import url, include
from django.contrib import admin

from sare.core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^questionario/', include('sare.questionarios.urls',
                                   namespace='questionarios')),
    url(r'^admin/', admin.site.urls),
]