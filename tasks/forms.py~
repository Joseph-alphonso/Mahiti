from django.db import models
from django import forms
from models import *




class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={'cols':110,'rows':1}),required=True)
    status = forms.ModelChoiceField(queryset=Task_Statuses.objects.all(),initial='Open',widget=forms.Select(attrs={'data-rel':'chosen'}),)
    priority = forms.ModelChoiceField(queryset=Task_priorities.objects.all(),\
                                                    initial='Medium')
    assigned_to = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.all(),
                                                                required=False)
    owned_by = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.all(),)
    followed_by = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.all(),
                                                                required=False)
    client = forms.ModelChoiceField(queryset=Client.objects.all(),empty_label='Choose a client',
                                                                required=False)
    module = forms.ModelChoiceField(queryset=Modules.objects.all(),
                                                    empty_label='Choose a module')
    milestone = forms.ModelChoiceField(queryset=Milestone.objects.all(),empty_label='Choose a Milestone',required=False)
    project = forms.ModelChoiceField(queryset=Project.objects.all(),
                                                empty_label='Choose a project')
    summary     = forms.CharField(widget=forms.Textarea(attrs={'cols': 110, 'rows': 10}),required=False)
    bug_reports = forms.FileField(label='Upload a Document',required=False)
    
    
    
    class Meta:
        model = Tasks
        widgets = {
        'due_date': forms.DateInput(attrs={'class':'datepicker'}),
        'start_date': forms.DateInput(attrs={'class':'datepicker'}),
        }



class RequestForm(forms.ModelForm):



    class Meta:
        model = Request
        widgets = {
        'requested_due_date': forms.DateInput(attrs={'class':'datepicker'}),
        }
