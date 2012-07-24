import urllib
import base64
from my_auth.models import User
from django.http import HttpResponseRedirect

#def test_login(view_func):
def login_required(view_func):
    def new(request, *args, **kwargs):
        s = request.session.get('my_au',None)
        if s is None:
            return HttpResponseRedirect('/accounts/login/?'+ urllib.urlencode({'redirect_to':request.path}))
        s = base64.decodestring(s).split(';')[0].split('=')[1]
        u = User.objects.filter(id=s)
        #u = request.session.get('my_au',None)
        if u:
            request.user=u[0]
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/accounts/login/?'+ urllib.urlencode({'redirect_to':request.path}))
    return new

#def login_required(function=None):
#    actual_decorator
