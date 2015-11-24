from django.db import models
from apps.myauth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    class Meta:
        db_table = 'movies'

class Watch_List(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)
    class Meta:
        db_table = 'watch_lists'