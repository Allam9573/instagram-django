from django.contrib import admin
from . models import Comment, Post
from users.models import User
# Register your models here.

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(User)
