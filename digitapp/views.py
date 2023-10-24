from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
from .models import *
import random


def index(request):
    labs = Lab.objects.all()
    all_fields = []
    for lab in labs:
        lab_fields = lab.fields.split(',')
        for lf in lab_fields:
            all_fields.append(lf) 
    
    best_projects = Project.objects.all().select_related('lab')[:3]
    context = {
        'all_fields': all_fields,
        'best_projects': best_projects,
    }
    return render(request, 'index.html', context)


def how(request):
    return render(request, 'how.html')


def lab(request, lab_slug):
    lab = Lab.objects.get(slug=lab_slug)
    lab_fields = lab.fields.split(',')
    context = {
        'lab': lab,
        'lab_fields': lab_fields
    }
    return render(request, 'lab.html', context)
def projects(request, lab_slug):
    lab = Lab.objects.get(slug=lab_slug)
    projects = Project.objects.filter(lab=lab)
    context = {
        'projects': projects,
        'lab': lab,

    }
    return render(request, 'projects.html', context)

def project(request, lab_slug, project_slug):
    lab = Lab.objects.get(slug=lab_slug)
    project = Project.objects.get(slug=project_slug)
    context = {
        'lab': lab,
        'project': project,
    }
    return render(request, 'project.html', context)


def about(request):
    labs = Lab.objects.all()
    all_fields = []
    for l in labs:
        all_fields += l.fields.split(',')
    context = {
        'lab': lab,
        'all_fields': random.sample(all_fields, 6)
    }
    return render(request, 'about.html', context)

def contacts(request):
    return render(request, 'contacts.html')

def contact_form(request):
    if request.method == 'POST':
        Application.objects.create(full_name=request.POST['fullname'],
                                   email=request.POST['email'],
                                   phone=request.POST['phone'],
                                   topic=request.POST['subject'],
                                   message=request.POST['message'])
    return redirect('contacts')

def mailing_form(request):
    if request.method == 'POST':
        Mailing.objects.create(email=request.POST['email'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))