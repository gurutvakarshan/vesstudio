from django.conf.urls import patterns, include, url

urlpatterns = patterns('DjangoProject.App.views.account',
    # Examples:
    # url(r'^$', 'DjangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^[/]$','registration',name='registration'),
    url(r'^/login/$','member_login',name='member_login'),
    url(r'^logout/$','member_logout',name='member_logout'),
    url(r'^activation/complete$','activation',name='activation'),
    url(r'^activation_email/$','activation_email',name='activation_email'),
    url(r'^reset_password/$','reset_password',name='reset_password'),
    url(r'^success/$','success',name='success'),
)