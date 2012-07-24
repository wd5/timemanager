from django import forms
from testing.models import Project, TestPage

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('created',)

class TestPageForm(forms.ModelForm):
    html = forms.CharField(required=True,widget=forms.Textarea(attrs={'style':'width:100%;height:400px;'}))
    
    class Meta:
        model = TestPage
        exclude = ('created','project')

      
