from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def posts(request):
    return HttpResponse('hola posts')


def listar_posts(request):
    return HttpResponse('listado de posts')


def post_id(request, id):
    return HttpResponse(f'Post {id}')
