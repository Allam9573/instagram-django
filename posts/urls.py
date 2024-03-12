from django.urls import path
from . import views

urlpatterns = [
    # path('', views.posts, name='posts'),
    path('<int:id>/', views.post_id, name='post_id'),
    path('api/save/', views.save_comment, name='save_comment')
]
