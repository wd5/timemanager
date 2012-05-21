# -*- coding: utf-8 -*-
 
from django.conf import settings

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson

from django.db.models import Max, Min

#from django.contrib.auth.decorators import login_required
from my_auth.decorators import login_required

from account.models import WallTask, ActiveTask
from my_auth.models import User
import base64
from datetime import datetime
import time
from my_auth.forms import SignUp


@login_required
def main_page(request):
    s = base64.decodestring(request.session['my_au']).split(';')[0].split('=')[1]
    u = get_object_or_404(User,id=s)
    context={'user':u}
    return render_to_response('html/accounts.html',
                              context,
                              context_instance=RequestContext(request))

@login_required
def wall_page(request):
    s = base64.decodestring(request.session['my_au']).split(';')[0].split('=')[1]
    u = get_object_or_404(User,id=s)
    context={'user':u}
    context['tasks'] = WallTask.objects.filter(owner=u)
    active_tasks = ActiveTask.objects.filter(user=u,end__isnull=True)
    context['active_task'] = -1
    if active_tasks:
        t = active_tasks[0]
        context['active_task'] = t.task.id
    
    return render_to_response('html/wall.html',
                              context,
                              context_instance=RequestContext(request))

@login_required
def add_wall_task(request):
    errors = []
    d = {}
    s = base64.decodestring(request.session['my_au']).split(';')[0].split('=')[1]
    u = User.objects.filter(id=int(s))
    if not u:
        errors.append('Вы должны авторизоваться')
    else:
        u=u[0]
    try:
        d['title'] = request.GET['title']
        d['text'] = request.GET['text']
        d['x'] = request.GET['x']
        d['y'] = request.GET['y']
    except:
        errors.append('Указаны не все параметры!')
    if not errors:
        wt=WallTask(title=d['title'],text_task=d['text'],position_x=d['x'],position_y=d['y'], owner=u)
        d['user'] = u.username
        wt.save()
        d['id'] = wt.id
    return HttpResponse(simplejson.dumps({'errors':errors,'data':d}),
                        mimetype='text/json')

@login_required
def del_wall_task(request,task_id):
    s = base64.decodestring(request.session['my_au']).split(';')[0].split('=')[1]
    u = User.objects.filter(id=int(s))
    if not u:
        errors.append('Вы должны авторизоваться')
    else:
        u=u[0]

    t = WallTask.objects.get(id=task_id,owner=u)
    t.delete();
    return HttpResponse('Ok',mimetype='text/plain')

@login_required
def update_wall_task(request,task_id):
    s = base64.decodestring(request.session['my_au']).split(';')[0].split('=')[1]
    u = User.objects.filter(id=int(s))
    if not u:
        errors.append('Вы должны авторизоваться')
    else:
        u=u[0]
    t = WallTask.objects.get(id=task_id,owner=u)
    if request.GET.has_key('x'):
        t.position_x=request.GET['x']
    if request.GET.has_key('y'):
        t.position_y=request.GET['y']
    if request.GET.has_key('text'):
        t.position_text_task=request.GET['text']
    if request.GET.has_key('title'):
        t.position_title=request.GET['title']
    t.save()
    return HttpResponse('Ok',mimetype='text/plain')    

def signup(request):
    if request.method=='POST':
        form = SignUp(request.POST)
        er = form.to_model()
        if er:
            for key in er:
                form.errors[key] = er[key]
            context = {'form' : form}
        else:
            return HttpResponseRedirect('/')
    if request.method=='GET':
        context = {'form' : SignUp()}
    return render_to_response('html/signup.html',
                              context,
                              context_instance=RequestContext(request))

@login_required
def activate_task(request,task_id):
    s = base64.decodestring(request.session['my_au']).split(';')[0].split('=')[1]
    u = get_object_or_404(User,id=s)
    t = WallTask.objects.get(id=task_id)
    active_tasks = ActiveTask.objects.filter(user=u,end__isnull=True)
    stop_task = -1
    if active_tasks:
        stop_task = active_tasks[0]
        stop_task.end = datetime.now()
        stop_task.length = time.mktime(stop_task.end.timetuple()) - time.mktime(stop_task.begin.timetuple())
        stop_task.save()
        stop_task = stop_task.task.id
    ActiveTask(user=u,task=t).save()
    return HttpResponse(simplejson.dumps({'error':False,
                                          'task_id':task_id,
                                          'stop_task_id':stop_task}),mimetype='text/json')

@login_required
def deactivate_task(request,task_id):
    s = base64.decodestring(request.session['my_au']).split(';')[0].split('=')[1]
    u = get_object_or_404(User,id=s)
    t = WallTask.objects.get(id=task_id)
    active_tasks = ActiveTask.objects.filter(user=u,task=t,end__isnull=True)
    if active_tasks:
        stop_task = active_tasks[0]
        stop_task.end = datetime.now()
        stop_task.length = time.mktime(stop_task.end.timetuple()) - time.mktime(stop_task.begin.timetuple())
        stop_task.save()
    return HttpResponse(simplejson.dumps({'error':False,
                                          'task_id':task_id}),mimetype='text/json')

@login_required
def statictic_by_wall_task(request,task_id):
    s = base64.decodestring(request.session['my_au']).split(';')[0].split('=')[1]
    u = get_object_or_404(User,id=s)
    t = WallTask.objects.get(id=task_id)
    if t.owner!=u:
        return HttpResponseNotFound()
    active_tasks = ActiveTask.objects.filter(task=t,end__isnull=False)
    all_time = 0
    period_activiti = None
    if active_tasks:
        if active_tasks.count()>1:
            all_time = reduce(lambda x,y:x.length+y.length,active_tasks)
        else:
            all_time = active_tasks[0].length
        period_activiti = [min(map(lambda x:x.begin,active_tasks)),
                           max(map(lambda x:x.end,active_tasks))
                           ]

    str_all_time = ' %ss'%str(all_time%60)
    if all_time>60:
        all_time = all_time/60
        str_all_time = ' %sm'%str(all_time%60) + str_all_time
        if all_time>60:
            all_time = all_time/60
            str_all_time = ' %sh'%str(all_time%24) + str_all_time
            if all_time>24:
                str_all_time = ' %sd'%str(all_time) + str_all_time
            
            
        
    context={'task':t,
             'user':u,
             'all_time':str_all_time,
             'period_activiti':period_activiti}
    return render_to_response('html/statistic-by-task.html',
                              context,
                              context_instance=RequestContext(request))
