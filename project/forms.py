from django import forms

from project.models import Project


# Linked to create_new_project.html
class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'project_name',
            'description',
            'featured_image',
            'client_name',
            'alt_image',
            'location',
            'finished',
            'tagline'
            ]


# Linked to edit_project.html
class UpdateProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'project_name',
            'description',
            'featured_image',
            'client_name',
            'alt_image',
            'location',
            'finished',
            'tagline'
            ]
