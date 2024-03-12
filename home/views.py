from django.shortcuts import render, HttpResponse
from posts.models import Post
from comments.models import Comment
# Create your views here.


def home(request):
    try:
        posts = Post.objects.all()
        comments = Comment.objects.all()
        return render(request, 'home.html', {
            'posts': posts,
            'comments': comments
        })
    except:
        return HttpResponse('No hay posts publicados')


def save_comment(request):
    pass
