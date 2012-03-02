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
                       url(r'^accounts/login/$','django.contrib.auth.views.login',
                           { 'template_name' : 'html/login.html',
                             'authentication_form' : LoginForm},
                           name="account_login"),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
                           { 'next_page' : '/' }, name="account_logout"),
                       )


#urlpatterns += patterns('',
#                        (r'^media/(?P<path>.*)$', 'django.views.static.serve' ,
#                         { 'document_root' : settings.MEDIA_ROOT })
#                        )

