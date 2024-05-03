from django.db import models
from django.utils import timezone
import datetime

class Movie(models.Model):
    title = models.CharField(max_length=200)
    star = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_more_than_200_number(self):
        return len(self.question_text) > 200

class Canvas(models.Model):
    pixel_color = models.CharField(max_length=200)