from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns(
    'testing.views',
    url(r'^$','index', name='testing_index'),
    url(r'^(?P<project_id>\d+)/add/$','add_testpage', name='testing_add_testpage'),
    url(r'^(?P<project_id>\d+)/(?P<page_id>\d+)/edit/$','edit_testpage', name='testing_edit_testpage'),
    url(r'^add/$','add_project', name='testing_add_project'),
    url(r'^(?P<project_id>\d+)/$','view_project', name='testing_view_project'),
    url(r'^view-test-page/(?P<slug>[\d\w_]+)$','view_testpage', name='testing_view_testpage'),
    )
