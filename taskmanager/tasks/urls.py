from django.urls import path, include
from . import views
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('login/', index, name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('list/', views.task_list, name='task_list'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('task/delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'), 
    path('register/', register_view, name='register'), 
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]

