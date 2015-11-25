from django.conf.urls import include, url, patterns
from apps.movies import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^/show', views.show, name = 'show'),
)
