from django.urls import path

from project.views import (

    create_project_view,
    edit_project,
    delete_project,

)

app_name = 'project'

urlpatterns = [

    path('create/', create_project_view, name='create'),
    path('edit/<slug>', edit_project, name='edit'),
    path('delete/<slug>', delete_project, name='delete'),

]
