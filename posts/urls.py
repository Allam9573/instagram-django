from django.urls import path
from . import views

urlpatterns = [
    # path('', views.posts, name='posts'),
    path('<int:id>/', views.post_id, name='post_id')
]
