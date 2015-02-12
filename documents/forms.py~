from django.forms import ModelForm
from django import forms
from documents.models import Document
from tasks.models import *

class DocumentForm(forms.Form):
    title = forms.CharField(required=True)
    files = forms.FileField(label='Upload a Document',required=False)
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    milestone = forms.ModelChoiceField(label='Milestone Document', queryset = Milestone.objects.all(), required=False)
    tasks = forms.ModelChoiceField(label='Task Document', queryset = Tasks.objects.all(), required=False)
    tags = forms.CharField(required=False)
    notes = forms.CharField(widget=forms.Textarea(attrs={'cols': 110, 'rows': 10}), required=False)



class TaskDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ['content_type', 'objects_id', 'active', 'optional_information']
