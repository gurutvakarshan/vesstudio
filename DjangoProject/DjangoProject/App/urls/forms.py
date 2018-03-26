from django.conf.urls import patterns, include, url

urlpatterns = patterns('DjangoProject.App.views.forms',
    # Examples:
    # url(r'^$', 'DjangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/$','forms',name='forms'),
    url(r'^/activities/fill_marks/academic/$','level1',name='level1'),
    url(r'^/activities/fill_marks/co_curricular/$','level2',name='level2'),
    url(r'^/activities/fill_marks/extra_curricular/$','level3',name='level3'),
    url(r'^/activities/fill_marks/sports/$','level4',name='level4'),
    url(r'^/activities/fill_marks/others/$','level5',name='level5'),
    url(r'^/activities/fill_marks/enrolled_in/$','level6',name='level6'),
    url(r'^/schedule/set_schedule/$','schedule',name='schedule'),
    url(r'^/notification/nofity/$','notification',name='notification')
)