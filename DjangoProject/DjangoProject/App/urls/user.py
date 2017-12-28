from django.conf.urls import patterns, include, url

urlpatterns = patterns('DjangoProject.App.views.user',
    # Examples:
    # url(r'^$', 'DjangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^[/]$','User',name='User'),
    url(r'^/data/$','data',name='data'),
)
