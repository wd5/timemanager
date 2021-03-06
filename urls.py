from django.conf import settings
from django.contrib import admin
from django.conf.urls.defaults import *
from django.views.static import serve

from middleware import index

from account.forms import LoginForm


urlpatterns = patterns('',
                       (r'^$','middleware.index'),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^accounts/',include('account.urls')),
#                       url(r'^accounts/login/$','django.contrib.auth.views.login',
#                           { 'template_name' : 'html/login.html',
#                             'authentication_form' : LoginForm},
                       url(r'^accounts/login/$','my_auth.views.login',
                           name="account_login"),
                       url(r'^accounts/logout/$', 'my_auth.views.logout', #,django.contrib.auth.views.logout',
                           name="account_logout"),
                       (r'^testing/',include('testing.urls')),
                       )


#urlpatterns += patterns('',
#                        (r'^media/(?P<path>.*)$', 'django.views.static.serve' ,
#                         { 'document_root' : settings.MEDIA_ROOT })
#                        )

