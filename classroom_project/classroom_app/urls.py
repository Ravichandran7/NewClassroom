from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_classroom, name='create_classroom'),
    path('join/', views.join_classroom, name='join_classroom'),
]
