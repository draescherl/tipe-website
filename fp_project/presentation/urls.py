from django.conf.urls import url

from . import views

#currently not in use

app_name = 'presentation'
urlpatterns = [
    url(r'^$', views.index, name='slides'),
]