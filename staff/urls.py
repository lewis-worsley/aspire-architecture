from django.urls import path

from . import views



urlpatterns = [
    path('login_staff_user', views.login_staff_user, name='login')
]
