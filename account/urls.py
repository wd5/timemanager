from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('account.views',
                       url(r'^$','main_page', name='account_main_page'),
                       url(r'wall/$','wall_page', name='account_wall_page'),
                       
                       )
