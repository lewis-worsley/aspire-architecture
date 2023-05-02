from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
# from django.contrib import messages

from project.models import Project
from project.forms import ProjectForm, UpdateProjectForm

# Create your views here.

def home_view(request):

    context = {}

    context['listOne'] = Project.objects.filter(finished=False)[:3]
    context['listTwo'] = Project.objects.filter(finished=True)[:3]

    return render(request, 'project/home.html', context)

def create_project_view(request):

    if request.method == "POST":
        form = ProjectForm(request.POST or None, request.FILES or None)

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
        form = UpdateProjectForm(request.POST or None, request.FILES or None, instance=project)
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


def delete_project(request, slug):
    
    project = get_object_or_404(Project, slug=slug)

    context = {'project': project}

    if request.method == "GET":
        return render(request, 'project/delete_project.html', context)
    elif request.method == "POST":
        project.delete()
        # messages.success(request, "Customise later")
        return redirect('home')


    
