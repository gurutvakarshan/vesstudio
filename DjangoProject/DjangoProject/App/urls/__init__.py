from django.conf.urls import patterns, include, url
from DjangoProject.App.views.landing_page import landing_page

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^captcha/', include('captcha.urls')),
    url(r'^$', landing_page, name='landing_page'),
    # (r'^account', include('DjangoProject.App.urls.account')),
    # (r'^captcha', include('DjangoProject.App.urls.captcha')),
    (r'^academic',include('DjangoProject.App.urls.academic_record')),
    (r'^user',include('DjangoProject.App.urls.user')),
    (r'^prouser',include('DjangoProject.App.urls.prouser')),

   )