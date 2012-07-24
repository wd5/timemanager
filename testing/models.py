# -*- coding:utf-8 -*-
from django.db import models
from my_auth.models import User

from default_html import DEFAULT_HTML

class Project(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)

class TestPage(models.Model):
    project = models.ForeignKey(Project)
    slug = models.CharField('Идентифокатор',max_length=32,blank=False)
    html = models.TextField('Код страницы',default = DEFAULT_HTML)
    permissions =  models.CharField(u'Права доступа',
                                    max_length=1,
                                    choices=(('0','Только для вадельца'),
                                             ('2','Только для авторизованных пользователей'),
                                             ('2','Для любого пользователя'),
                                             ),
                                    default='0')
    created = models.DateTimeField(auto_now_add=True)

    
