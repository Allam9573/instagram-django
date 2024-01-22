from django.shortcuts import render
from django.contrib.auth import base_user

# Create your views here.


def login_user(request):
    return render(request, 'login.html')


def sign(request):
    print(base_user)
    return render(request, 'sign.html')

