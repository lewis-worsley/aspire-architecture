from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

import re

from .forms import RegisterStaffUserForm


def login_staff_user(request):
    """
    Logs users in

    """

    user = request.user

    if user.is_staff:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Login successful! Hello {username}.")
            return redirect('home')
        else:
            messages.error(
                request, "Invalid username or password.")
            return redirect('login')

    else:
        return render(request, 'staff/login.html', {})


def logout_staff_user(request):
    """
    Logs out users

    """

    logout(request)
    messages.success(request, "You're now logged out!")
    return redirect('home')


def register_staff_user(request):
    """
    Register new users

    """

    user = request.user

    if user.is_staff:
        return redirect('home')

    if request.method == "POST":
        form = RegisterStaffUserForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']

            # Check if email matches the desired pattern
            pattern = r'^\w+@aspire\.com$'

            if not re.match(pattern, email):
                return render(request, 'staff/register.html', {'form': form})

            form.save()
            messages.info(
                request, "Account pending approval. Admin has been notified.")
            return redirect('home')

    else:
        form = RegisterStaffUserForm()

    return render(request, 'staff/register.html', {'form': form})
