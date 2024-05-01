from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    star = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)