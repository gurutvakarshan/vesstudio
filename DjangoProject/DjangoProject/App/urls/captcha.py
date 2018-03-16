from django.conf.urls import patterns, include, url

urlpatterns = patterns('DjangoProject.App.views.captcha',
    # Examples:
    # url(r'^$', 'DjangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^[/]$','some_view',name='some_view'),
)