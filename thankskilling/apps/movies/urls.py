from django.conf.urls import include, url, patterns
from apps.movies import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^/show/(?P<movie_id>\d+)/$', views.show, name = 'show'),
    url(r'^/watch_list$', views.watch_list, name = 'watch_list'),
    url(r'^/add/(?P<movie_id>\d+)/$', views.add_to_list, name='add'),
)
