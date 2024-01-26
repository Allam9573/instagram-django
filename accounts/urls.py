from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('sign/', views.sign, name='sign'),
    path('creare-account/', views.create_account, name='create_account')
]
