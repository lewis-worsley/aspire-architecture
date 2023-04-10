from django.shortcuts import render

from project.models import Project
from project.forms import CreateNewProjectForm

# Create your views here.

# def home_view(request):
#     return render(request, 'base.html')

def home_view(request):

    context = {}

    projects = Project.objects.all
    context['projects'] = projects

    return render(request, 'project/home.html', context)

def create_project_view(request):

    context = {}

    form = CreateNewProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CreateNewProjectForm()

    context['form'] = form

    return render(request, 'project/create_new_project.html', {})