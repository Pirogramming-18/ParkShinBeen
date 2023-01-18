from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.idea_list, name="idea_list"),
    path('tool/create', views.tool_create, name="tool_create"),
    path('tool/list', views.tool_list, name="tool_list"),
    path('tool/<int:pk>', views.tool_detail, name="tool_detail"),
    path('tool/<int:pk>/update', views.tool_update, name="tool_update"),
    path('tool/<int:pk>/delete', views.tool_delete, name="tool_delete"),
    path('idea/create', views.idea_create, name="idea_create"),
    path('idea/<int:pk>', views.idea_detail, name="idea_detail"),
    path('idea/<int:pk>/update', views.idea_update, name="idea_update"),
    path('idea/<int:pk>/delete', views.idea_delete, name="idea_delete"),
]