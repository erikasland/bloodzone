from django.conf.urls import include, url, patterns
from apps.myauth import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
    )