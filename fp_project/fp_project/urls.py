"""fp_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from presentation import views as presentation_views

urlpatterns = [
    # Admin page :
    url(r'^admin/', admin.site.urls),
    
    # Default home page :
    url(r'^$', presentation_views.home, name='home'),
    
    # Login page :
    url(r'^login/$', auth_views.LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    
    # Logout page :
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': 'login'}, name='logout'),
    
    # Signup page :
    #url(r'^signup/$', presentation_views.signup, name='signup'),
    #do not forget to add signup elements back in template if needed

    # Slide views :
    url(r'^presentation/', include('presentation.urls', namespace='presentation')),

    #url(r'^$', presentation_views.index, name='index'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns