from django.shortcuts import render, HttpResponse
from posts.models import Post

# Create your views here.


def home(request):
    try:
        posts = Post.objects.all()
        return render(request, 'home.html', {
            'posts': posts
        })
    except:
        return HttpResponse('No hay posts publicados')
