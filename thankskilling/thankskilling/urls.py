
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('apps.myauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
