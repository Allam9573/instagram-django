from django.shortcuts import render
from users.models import User
# Create your views here.


def profile(request):
    user = User.objects.get(pk=1)
    return render(request, 'profile.html', {
        'user': user
    })
