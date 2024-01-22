from django.shortcuts import render
from .models import Post

# Create your views here.


# def posts(request):
#     posts = Post.objects.all()
#     return render(request, 'posts.html', {
#         'posts': posts
#     })

def post_id(request, id):
    try:
        posts = Post.objects.get(pk=id)
        return render(request, 'posts.html', {
            'posts': posts,
        })
    except:
        return render(request, 'posts.html')
