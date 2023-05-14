from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def login_staff_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.warning(request, "Error occured. Login details incorrect. Invalid username or password")
            return redirect('login')

    else:
        return render(request, 'staff/login.html', {})


def logout_staff_user(request):
    logout(request)
    messages.success(request, "You're now logged out!")
    return redirect('home')


def register_staff_user(request):
    if request.method == "POST":
        form = UserCreationForm()(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Account registered")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'staff/register.html', {
        'form': form
    })