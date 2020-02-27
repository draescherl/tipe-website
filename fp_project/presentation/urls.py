from django.conf.urls import url

from . import views

app_name = 'presentation'
urlpatterns = [
    url(r'^(?P<slide_id>[0-9]+)/$', views.slide, name='slide'),
]