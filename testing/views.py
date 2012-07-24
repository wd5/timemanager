# -*- coding: utf-8 -*-
 
from django.conf import settings

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from my_auth.decorators import login_required
from testing.models import Project, TestPage
from testing.forms import ProjectForm, TestPageForm
from default_html import DEFAULT_HTML

from django.core.urlresolvers import reverse

@login_required
def index(request):    
    return render_to_response('html/testing/index.html',
                              {'user':request.user,
                               'projects':Project.objects.filter(owner=request.user),
                               },
                              context_instance=RequestContext(request))

@login_required
def add_project(request):
    if request.method == 'GET':
        form=ProjectForm()
    else:
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/testing/')
    return render_to_response('html/testing/add_project.html',
                              {'user':request.user,
                               'form':form,
                               },
                              context_instance=RequestContext(request))

@login_required
def view_project(request,project_id):
    project = get_object_or_404(Project,id=project_id)
    if project.owner.id != request.user.id:
        return HttpResponseNotFound()    
    return render_to_response('html/testing/view_project.html',
                              {'user':request.user,
                               'project':project,
                               },
                              context_instance=RequestContext(request))
    
    
@login_required
def add_testpage(request,project_id):
    project = get_object_or_404(Project,id=project_id)
    if project.owner.id != request.user.id:
        return HttpResponseNotFound()        
    if request.method == 'GET':
        form=TestPageForm(initial = {'html' : DEFAULT_HTML})
    else:
        form=TestPageForm(request.POST)
        if form.is_valid():
            form.instance.project = project
            form.save()
            #form.instance.save()
            return HttpResponseRedirect(reverse(view_project, args=[project_id]))
    return render_to_response('html/testing/add_project.html',
                              {'user':request.user,
                               'form':form,
                               },
                              context_instance=RequestContext(request)
                              )

@login_required
def edit_testpage(request,project_id,page_id):
    page = get_object_or_404(TestPage,id=page_id)
    project = page.project
    if project.owner.id != request.user.id:
        return HttpResponseNotFound()        
    if request.method == 'GET':
        form=TestPageForm(instance=page)
    else:
        form=TestPageForm(request.POST,instance=page)
        if form.is_valid():
            form.instance.project = project
            form.save()
            #form.instance.save()
            return HttpResponseRedirect(reverse(view_project, args=[project_id]))
    return render_to_response('html/testing/add_project.html',
                              {'user':request.user,
                               'form':form,
                               },
                              context_instance=RequestContext(request)
                              )


def view_testpage(request,slug):
    #return HttpResponse(slug)
    return HttpResponse(TestPage.objects.get(slug=slug).html)
