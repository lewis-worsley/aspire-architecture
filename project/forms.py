from django import forms

from project.models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'project_name', 
            'description', 
            'client_name', 
            'location', 
            'tagline'
            ]

class UpdateProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'project_name', 
            'description', 
            'client_name', 
            'location', 
            'tagline'
            ]
    
    def save(self, commit=True):
        project = self.instance
        project.project_name = self.cleaned_data['project_name']
        project.description = self.cleaned_data['description']
        project.client_name = self.cleaned_data['client_name']
        project.location = self.cleaned_data['location']
        project.tagline = self.cleaned_data['tagline']

        if commit:
            project.save()
        return project