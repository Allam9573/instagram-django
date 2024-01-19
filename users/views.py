from django.shortcuts import render, HttpResponse

# Create your views here.


def lista_usuarios(request):
    return HttpResponse(f'Lista usuarios')
