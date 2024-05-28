from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
            )
            auth.login(request, user)
            return redirect('list')
        return render(request, 'signup.html')
    return render(request, 'singup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')