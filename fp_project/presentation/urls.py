from django.conf.urls import url

from . import views

app_name = 'presentation'
urlpatterns = [
    url(r'^$', views.slides, name='slides'),
]