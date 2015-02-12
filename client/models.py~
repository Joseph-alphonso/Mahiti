from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
import datetime
from django.utils.translation import gettext as _


class Base(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Client(Base):
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=2, blank=True, null=True)
    address = models.TextField(blank=True, null=True, max_length=100)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True, max_length=100)

    def __unicode__(self):
        return self.name

    def get_projects(self):
        from projects.models import Project
        projects = Project.objects.filter(client=self)
        return projects

    def get_active_projects(self):
        from projects.models import Project
        active_projects = Project.objects.filter(client=self, active=2).count()
        return active_projects

    def get_project_name(self):
        from projects.models import Project
        project = Project.objects.get(client=self)
        return  project.name

    def get_user_profile(self):
        from people.models import UserProfile
        people = UserProfile.objects.filter(client=self)
        return people

    def get_task_list(self):
        from tasks.models import Tasks
        task = Tasks.objects.filter(client=self)
        return task

    def get_user_profilelist(self):
        from people.models import UserProfile
        users = UserProfile.objects.filter(client=self)
        print users, "users"
        return users



class CSVFiles(Base):

    upload_file = models.FileField(upload_to="csv", blank=True, null=True)



class Recently_Viewed(models.Model):

    user = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType, blank=True, null=True,
                                     verbose_name=_('content type'),
                             related_name='Content_Type_Of_Recently_Viewed')
    object_id = models.TextField(_('object ID'), blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    created_on = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return '%s' %(self.user.first_name)





