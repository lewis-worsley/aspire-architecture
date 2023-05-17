from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

import re

from .forms import RegisterStaffUserForm


# Linked to login.html
def login_staff_user(request):

    user = request.user

    if user.is_staff:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success
            (request,
                f"Login successful! Hello {username}.")
            return redirect('home')
        else:
            messages.error
            (request,
                "Login details incorrect. Invalid username or password.")
            return redirect('login')

    else:
        return render(request, 'staff/login.html', {})


# Not linked to any page but logout can be found in the footer
def logout_staff_user(request):
    logout(request)
    messages.success(request, "You're now logged out!")
    return redirect('home')


# Linked to register.html
def register_staff_user(request):

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
                messages.error
                (request,
                    "Invalid email address. Please use the @aspire.com domain")
                return render(request, 'staff/register.html', {'form': form})

            form.save()
            messages.info
            (request,
                "Account pending approval. Admin has been notified.")
            return redirect('home')

    else:
        form = RegisterStaffUserForm()

    return render(request, 'staff/register.html', {'form': form})
