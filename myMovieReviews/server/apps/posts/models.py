from django.db import models

class Post(models.Model):

    MOVIE_GENRE = (
        ('AC','액션'),
        ('CR','범죄'),
        ('SF','SF'),
        ('CO','코미디'),
        ('RC','로맨스 코미디'),
        ('RO','로맨스'),
        ('ME','멜로'),
        ('TH','스릴러'),
        ('HO','공포'),
        ('WA','전쟁'),
        ('SP','스포츠'),
        ('FA','판타지'),
        ('MU','음악'),
        ('DR', '드라마'),
    )

    title = models.CharField(max_length=64)
    year = models.IntegerField()
    director = models.CharField(max_length=32)
    main_actor = models.CharField(max_length=32)
    genre = models.CharField(max_length=2, choices=MOVIE_GENRE)
    rate = models.FloatField()
    running_time = models.IntegerField()
    review = models.TextField()
    image = models.CharField(max_length=512, default='https://ssl.pstatic.net/static/movie/2012/06/dft_img77x110_1.png')