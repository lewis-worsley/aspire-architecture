from django.urls import path
from project.views import (

    create_project_view,

)

app_name = 'project'

urlpatterns = [
    path('create/', create_project_view, name="create")
]