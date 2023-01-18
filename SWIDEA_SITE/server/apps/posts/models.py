from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    content = models.TextField()


class Idea(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='ideas/%Y%m%d')
    content = models.TextField()
    interest = models.IntegerField(default=0)
    devtool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True)