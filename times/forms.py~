from django.db import models
from django import forms
from times.models import *



class AddTimeForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=UserProfile.objects.all(),
                                    empty_label='Choose a person')
    client = forms.ModelChoiceField(queryset=Client.objects.all(),
                                    empty_label='Choose a client',
                                    required=False)
    project = forms.ModelChoiceField(queryset=Project.objects.all(),
                                    empty_label='Choose a project')
    module = forms.ModelChoiceField(queryset=Modules.objects.all(),
                                    empty_label='Choose a module')
    tasks = forms.ModelChoiceField(queryset=Tasks.objects.all(),
                                    empty_label='Choose a task')
    worktype = forms.ModelChoiceField(queryset=Work_Type.objects.all())
    

    class Meta:
        model = AddTime
        exclude = ('status_view',)
        widgets = {
        'pub_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }

