from django.conf.urls import patterns, include, url

urlpatterns = patterns('DjangoProject.App.views.academic_record',
    # Examples:
    # url(r'^$', 'DjangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^[/]$','academic',name='academic'),
)

