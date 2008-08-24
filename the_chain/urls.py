from django.conf.urls.defaults import *

urlpatterns = patterns('dont_break_the_chain.the_chain.views',
    (r'^(?P<calendar_id>\d+)/$', 'show'),
)
