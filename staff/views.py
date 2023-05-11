from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_staff_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "Error occured. Login details incorrect")
            return redirect('login')
    
    else:
            # Return an 'invalid login' error message.
        return render(request, 'staff/login.html', {})

