from django.shortcuts import render
from django.utils.text import slugify

from project.models import Project
from project.forms import CreateNewProjectForm

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
        form = CreateNewProjectForm(request.POST)

        if form.is_valid():
            # project_name = form.cleaned_data["project_name"]
            # description = form.cleaned_data["description"]
            # client_name = form.cleaned_data["client_name"]
            # location = form.cleaned_data["location"]
            # tagline = form.cleaned_data["tagline"]
            project = form.save(commit=False)
            project.slug = slugify(project.project_name)
            project.save()    

    form = CreateNewProjectForm()
    context = {
        'form': form
    }

    return render(request, 'project/create_new_project.html', context)