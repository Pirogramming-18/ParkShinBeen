from django.db import models

class Post(models.Model):
    user = models.CharField(max_length=30)
    content = models.TextField()
    like = models.IntegerField(default=0)
    pressed = models.BooleanField(default=False)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    content = models.TextField()