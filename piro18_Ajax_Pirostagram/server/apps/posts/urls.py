from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.main, name="main"),
    path('create', views.create, name="create"),
    path('like_ajax/', views.like_ajax, name="like_ajax"),
    path('comment_ajax/', views.comment_ajax, name="comment_ajax"),
    path('delete_ajax/', views.delete_ajax, name="delete_ajax"),
    path('delete/<int:pk>', views.delete, name="delete"),
]