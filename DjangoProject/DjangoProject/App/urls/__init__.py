from django.conf.urls import patterns, include, url
from DjangoProject.App.views.landing_page import landing_page
if landing_page:
	print "True"
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', landing_page, name='landing_page'),
    (r'^academic',include('DjangoProject.App.urls.academic_record')),
    (r'^user',include('DjangoProject.App.urls.user')),
    (r'^prouser',include('DjangoProject.App.urls.prouser')),

   )