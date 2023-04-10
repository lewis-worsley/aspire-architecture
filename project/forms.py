from django import forms

from project.models import Project

class CreateNewProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['project_name', 'description', 'client_name', 'location', 'tagline']