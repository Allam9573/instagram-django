from django.shortcuts import render, redirect
from django.contrib.auth import base_user
from ..users.models import User

# Create your views here.


def login_user(request):
    return render(request, 'login.html')


def sign(request):
    print(base_user)
    return render(request, 'sign.html')


def create_account(request):
    if request.method == "POST":
        email = request.POST['email']
        fullname = request.POST['fullname']
        username = request.POST['username']
        password = request.POST['password']
        try:
            new_user = User(
                email=email,
                fullname=fullname,
                username=username,
                password=password
            )
            new_user.save()
            return redirect('home')
        except:
            pass
