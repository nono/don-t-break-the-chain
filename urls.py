from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'dont_break_the_chain.the_chain.views.index'),
    (r'^calendar/', include('dont_break_the_chain.the_chain.urls')),
    (r'^admin/', include('django.contrib.admin.urls')),
)
