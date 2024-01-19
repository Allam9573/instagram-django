from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts),
    path('listado-posts', views.listar_posts),
    path('post/<int:id>/', views.post_id)
]
