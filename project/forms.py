from django import forms

from project.models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'project_name', 
            'description',
            'featured_image',
            'client_name', 
            'location',
            'finished',
            'tagline'
            ]

class UpdateProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'project_name', 
            'description',
            'featured_image',
            'client_name', 
            'location',
            'finished',
            'tagline'
            ]