from django.conf.urls import include, url, patterns
from apps.myauth import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^registration', views.registration, name='registration'),
        url(r'^login', views.login, name='login'),
        url(r'^logout$', views.logout, name='logout'),
         # url(r'^logout_auth', views.logout_auth, name='logout_auth'),

        # url(r'^success/(?P<uname>[\w|\W]+)/$', views.success, name='success'),
        url(r'^success', views.success, name='success'),
    )