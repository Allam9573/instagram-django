from django.shortcuts import render, redirect
from .models import Post
from comments.models import Comment
from users.models import User
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


def save_comment(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        comment = request.POST['comment']
        user = User.objects.get(id=int(user_id))
        new_comment = Comment(
            user=user,
            comment=comment
        )
        new_comment.save()
        return redirect('home')
    else:
        return redirect('home')
