from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

from account.models import WallTask

@login_required
def main_page(request):
    return render_to_response('html/accounts.html',
                              {},
                              context_instance=RequestContext(request))

@login_required
def wall_page(request):
    context = {'tasks':WallTask.objects.all()}
    return render_to_response('html/wall.html',
                              context,
                              context_instance=RequestContext(request))

def add_wall_task(request):
#    wt=WallTask(title='test',text_task='T',position_x=1,position_y=1)
#    wt.save()
    return HttpResponse('Ok',mimetype='text/plain')

def add_wall_task(request):
    wt=WallTask(title='test',text_task='TTTTTTTTTTTTTTT',position_x=1,position_y=1)
    wt.save()
    return HttpResponse('Ok',mimetype='text/plain')

def del_wall_task(request,task_id):
    t = WallTask.objects.get(id=task_id)
    if t:
        t.delete();
    return HttpResponse('Ok',mimetype='text/plain')
