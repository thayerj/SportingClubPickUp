from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spcball.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^reg/', include('morningreg.urls', namespace='reg')),
    url(r'^admin/', include(admin.site.urls)),
)
