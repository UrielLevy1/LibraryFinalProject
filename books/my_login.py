from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateuserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

    
def registration(request):
    form = CreateuserForm()
    if request.method == "POST":
        form = CreateuserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Successfully account created for " + user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html' ,context)    


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'books.html  ')
        else:
            messages.warning(request, "Sorry, this user is not exist, please try again!")
    context = {}
    return render(request, 'my_login.html', context)