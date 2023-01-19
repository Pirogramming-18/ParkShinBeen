from django.db import models
from django.conf import settings 

class Tool(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.name


class Idea(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='ideas/%Y%m%d')
    content = models.TextField()
    interest = models.IntegerField(default=0)
    devtool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True)
    like = models.IntegerField(default=0)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', null=True)