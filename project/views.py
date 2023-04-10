from django.shortcuts import render
from project.models import Project

# Create your views here.

# def home_view(request):
#     return render(request, 'base.html')

def home_view(request):

    context = {}

    projects = Project.objects.all
    context['projects'] = projects

    return render(request, 'project/projects.html', context)