from django.contrib import admin
from .models import Movie
from .models import Question

admin.site.register(Movie)

admin.site.register(Question)