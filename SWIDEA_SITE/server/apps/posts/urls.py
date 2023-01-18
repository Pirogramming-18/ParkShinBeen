from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list),
]