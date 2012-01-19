from django.conf.urls.defaults import patterns
from django.views.generic.simple import direct_to_template
from django.conf import settings

from main import views

urlpatterns = patterns('',
                       
    #Url configuration
    (r'^$', direct_to_template, {'template': 'smstest.html'}),
    (r'^sms', views.smssync),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    )
