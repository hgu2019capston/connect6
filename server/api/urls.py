from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^battle/', views.BattlePage, name='battle'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^resultdata/(?P<pk>[0-9]+)/$', views.ResultData),
    url(r'^getsession/$', views.getSession),
    url(r'^hello/$', views.helloworld),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
