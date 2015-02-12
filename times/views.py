from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.core.paginator  import Paginator,InvalidPage, EmptyPage
from django.http import HttpResponse,HttpResponseRedirect
from times.models import AddTime
from times.models import AddTime
from forms import *
from client.models import Client
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.template.defaultfilters import slugify
from tasks.models import Tasks
from datetime import *
from django.contrib.auth.decorators import login_required

# Create your views here.

import datetime
@login_required(login_url="/login/")
def addtimes(request):

    #tasks = Tasks.objects.latest('id')
    tasks = Tasks.objects.filter(status=1)
    form = AddTimeForm()
    user_id = request.user.id
    user_id2 = UserProfile.objects.get(user__id=user_id)
    todays = datetime.date.today()
    error = ''
    msg = ''
    nam = ''
    x = ''
    f = ''
    if request.method == 'POST':
        form = AddTimeForm(request.POST)
        name = request.POST.get('name', '')
        if form.is_valid():
            f = form.save(commit=False)
            f.slug=name
            f.save()
            msg = "successfully saved"
            return HttpResponseRedirect("/times/")
        else:
            error = "form error"
    return render(request,"times/tim.html", locals(), context_instance=RequestContext(request))


@login_required(login_url="/login/")
def addmtimes(request):

    form = AddTimeForm()
    subform = AddTimeForm(prefix="tim")
    subbform = AddTimeForm(prefix="tims")
    error = ''
    msg = ''
    nam = ''
    x = ''
    f = ''
    s = ''
    ss = ''
    messages = ''
    if request.method == 'POST':
        form = AddTimeForm(request.POST)
        subform = AddTimeForm(request.POST, prefix="tim")
        subbform = AddTimeForm(request.POST, prefix="tims")
        #form_description = request.POST('description','')
        #subform_description = request.POST('description','')
        #subbform_description = request.POST('description','')
        if form.is_valid() and subform.is_valid() and subbform.is_valid():
            f = form.save(commit=False)
            f.save()
            s = subform.save(commit=False)
            s.save()
            ss = subbform.save(commit=False)
            ss.save()
            msg = "successfully saved"
            return HttpResponseRedirect("/times/")
        else:
            error = "form error"
    return render(request,"times/mtim.html", locals(), context_instance=RequestContext(request))



@login_required(login_url="/login/")
def tim(request):

    timess = AddTime.objects.all()
    worktype = request.GET.get('Client search', '')
    times = timess
    return render(request, "times/index.html", locals())


@login_required(login_url="/login/")
def manage_time_sheets(request, task=None):

    msg = ''
    if task == "submit":
        id_submit = request.GET.get('id')
        time_obj = AddTime.objects.get(id=id_submit)
        time_obj.status_view = 1
        time_obj.save()
        msg = "Time sheet submitted"
        return HttpResponseRedirect("/times/manage/timesheets/")
    elif task == "approve":
        id_approve = request.GET.get('id')
        time_obj = AddTime.objects.get(id=id_approve)
        time_obj.status_view = 2
        time_obj.save()
        msg = "Time sheet approved"
        return HttpResponseRedirect("/times/manage/timesheets/")
    elif task == "reject":
        id_reject = request.GET.get('id')
        time_obj = AddTime.objects.get(id=id_reject)
        time_obj.status_view = 3
        time_obj.save()
        msg = "Time sheet rejected"
        return HttpResponseRedirect("/times/manage/timesheets/")
    else:
        return HttpResponseRedirect("/times/manage/timesheets/")
    return render(request, "times/manage_time.html", locals())


def manage_timesheets(request):

    userprofile_list = UserProfile.objects.all()
    user_obj = request.user.id
    times_person_obj = AddTime.objects.filter(person__id=user_obj)
    times_view_obj = times_person_obj.filter(status_view='0')
    times_submitted = times_person_obj.filter(status_view='1')
    times_approve = times_person_obj.filter(status_view='2')
    times_reject = times_person_obj.filter(status_view='3')
    return render(request,"times/manage-timesheets.html", locals())


@login_required(login_url="/login/")
def current_week(request):

    times = AddTime.objects.all()
    id_submit = request.GET.get('id_submit')
    curentweek_obj = AddTime.objects.get(id=id_submit)
    curentweek_obj.status_view = 2
    curentweek_obj.save()
    current_week = AddTime.objects.filter(status_view=2)
    #e=AddTime.objects.filter(status_view=2)
    return render(request, "times/manage_time.html", locals())


@login_required(login_url="/login/")
def activetimer(request):

    times = AddTime.objects.all()
    task = Tasks.objects.values('title').distinct()
    return render(request, "times/active_timers.html", locals())



@login_required(login_url="/login/")
def missingtime(request):

    date=request.GET.get('date', '')
    if date:
        times = AddTime.objects.filterQ(date__gte=date), Q(date__lte=date)
    return render(request, "times/missing_timesheets.html", locals())


@login_required(login_url="/login/")
def whg(request):

    times = AddTime.objects.all()
    return render(request, "times/weekly_hour_graph.html", locals())


@login_required(login_url="/login/")
def sub(request):

    times = AddTime.objects.all()
    return render(request, "times/submitted.html", locals())

@login_required(login_url="/login/")
def edittimes(request, id_edit):

    msg = ''
    times = AddTime.objects.get(id=id_edit)
    form = AddTimeForm(instance=times)
    if request.POST:
        form = AddTimeForm(request.POST, instance=times)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            edit_done = True
            msg = "edited successfully"
            success = True
            return HttpResponseRedirect("/times/")
        else:
             msg = 'Invalid form'
    return render(request, "times/tim.html", locals())



@login_required(login_url="/login/")
def timeview(request):

    disp = request.GET.get('id')
    tim = AddTime.objects.get(id=disp)
    return render(request, "times/time_view.html", locals())


@login_required(login_url="/login/")
def deletetimes(request, id_delete):

    p = AddTime.objects.get(id=id_delete)
    p.delete()
    return HttpResponseRedirect("/times/")


