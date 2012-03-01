from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from django.contrib.auth.decorators import login_required


@login_required
def main_page(request):
    return render_to_response('html/accounts.html',
                              {},
                              context_instance=RequestContext(request))

@login_required
def wall_page(request):
    return render_to_response('html/wall.html',
                              {},
                              context_instance=RequestContext(request))
