from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^index/', views.index),
    url(r'^resultdata/$', views.ResultData),
    url(r'^getsession/$', views.getSession),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
