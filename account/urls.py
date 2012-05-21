from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('account.views',
                       url(r'^$','main_page', name='account_main_page'),
                       url(r'signup/$', 'signup', name='add_user'),
                       url(r'wall/$','wall_page', name='account_wall_page'),
                       url(r'wall/add-task','add_wall_task', name='add_wall_task'),
                       url(r'wall/(?P<task_id>\d+)/del-task/','del_wall_task', name='del_wall_task'),
                       url(r'wall/(?P<task_id>\d+)/update-task/','update_wall_task', name='update_wall_task'),

                       url(r'wall/(?P<task_id>\d+)/deactivate/','deactivate_task', name='deactivate_task'),
                       url(r'wall/(?P<task_id>\d+)/activate/','activate_task', name='activate_task'),
                       url(r'wall/(?P<task_id>\d+)/statistic/','statictic_by_wall_task', name='statictic_by_wall_task'),
                       )
