from django.urls import path
from . import views
import uuid

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<uuid:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<uuid:pk>/edit/', views.post_edit, name='post_edit'),
]
