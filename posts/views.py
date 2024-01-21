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
        post = Post.objects.get(pk=id)
        comments = post.comments.all()
        return render(request, 'posts.html', {
            'posts': post,
            'comments': comments
        })
    except:
        return render(request, 'posts.html')
