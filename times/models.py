from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from projects.models import Project
from people.models import UserProfile
from tasks.models import Tasks
from client.models import Client
from mastermodule.models import Work_Type
from mastermodule.models import Modules

# Create your models here.


class AddTime(models.Model):
    person = models.ForeignKey(UserProfile)
    date = models.DateField(blank=True, null=True)
    times = models.FloatField(blank=True, null=True)
    client = models.ForeignKey(Client)
    project = models.ForeignKey(Project)
    module = models.ForeignKey(Modules)
    tasks = models.ForeignKey(Tasks, blank=True, null=True)
    worktype = models.ForeignKey(Work_Type)
    description = models.TextField(max_length=100, blank=True, null=True)
    billable = models.BooleanField()
    status_view = models.IntegerField(blank=True, null=True, default=0)

    def __unicode__(self):
        return self.tasks.title


    class Meta:
        ordering = ('times',)

