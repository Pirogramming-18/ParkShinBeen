from django.contrib import admin
from server.apps.posts.models import Tool, Idea

admin.site.register(Idea)
admin.site.register(Tool)