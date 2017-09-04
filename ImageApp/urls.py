from django.conf.urls import url, include
from ImageApp import views
from rest_framework.authtoken import views as Auth

urlpatterns = [
    url(r'^[index/]*$', views.index, name='index'),
    url(r'^image/$', views.ShowImages.as_view()),
    url(r'^image/(?P<img>(.*?))/$', views.ShowDetail.as_view()),
    url(r'^api-token-auth/$', Auth.obtain_auth_token)
]