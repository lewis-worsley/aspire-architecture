from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.contrib import messages

from project.models import Project
from project.forms import ProjectForm, UpdateProjectForm


def home_view(request):
    """
    Displays home view and creates queryset for projects

    """

    context = {}

    # Current Projects
    context['listOne'] = Project.objects.filter(finished=False)[:3]

    # Finished Projects
    context['listTwo'] = Project.objects.filter(finished=True)[:3]

    return render(request, 'project/home.html', context)


def create_project_view(request):
    """
    Creates a new project

    """

    if request.method == "POST":
        form = ProjectForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            item = form.save(commit=False)
            item.slug = slugify(item.project_name)
            item.save()
            messages.success(request, f"Project created: {item.project_name}")
            return redirect('/#projects')

    form = ProjectForm()
    context = {
        'form': form
    }

    return render(request, 'project/create_new_project.html', context)


def edit_project(request, slug):
    """
    Edits the projects

    """

    project = get_object_or_404(Project, slug=slug)

    if request.method == "POST":
        form = UpdateProjectForm(
             request.POST or None, request.FILES or None, instance=project)

        if form.is_valid():
            item = form.save(commit=False)
            item.slug = slugify(item.project_name)
            item.save()
            messages.success(request, f"Project updated: {item.project_name}")
            return redirect('/#projects')

    form = UpdateProjectForm(instance=project)
    context = {
        'form': form,
        'admin': True
    }

    return render(request, 'project/edit_project.html', context)


def delete_project(request, slug):
    """
    Delete projects

    """

    project = get_object_or_404(Project, slug=slug)

    context = {'project': project}

    if request.method == "GET":
        return render(request, 'project/delete_project.html', context)

    elif request.method == "POST":
        project.delete()
        messages.success(request, f"Project deleted: {project.project_name}")
        return redirect('/#projects')
