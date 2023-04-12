from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from project.models import Project
from project.forms import ProjectForm, UpdateProjectForm

# Create your views here.

# def home_view(request):
#     return render(request, 'base.html')

def home_view(request):

    context = {}

    projects = Project.objects.all()
    context['projects'] = projects

    return render(request, 'project/home.html', context)


def create_project_view(request):

    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.slug = slugify(item.project_name)
            item.save()
            return redirect('/')

    form = ProjectForm()
    context = {
        'form': form
    }

    return render(request, 'project/create_new_project.html', context)


def edit_project(request, slug):

    project = get_object_or_404(Project, slug=slug)

    if request.method == "POST":
        form = UpdateProjectForm(request.POST or None, instance=project)
        if form.is_valid():
            item = form.save(commit=False)
            item.slug = slugify(item.project_name)
            item.save()
            return redirect('/')

    form = UpdateProjectForm(instance=project)
    context = {
        'form': form
    }
    
    return render(request, 'project/edit_project.html', context)