from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=64)
    year = models.IntegerField()
    director = models.CharField(max_length=32)
    main_actor = models.CharField(max_length=32)
    genre = models.CharField(max_length=32)
    rate = models.FloatField()
    running_time = models.IntegerField()
    review = models.TextField()