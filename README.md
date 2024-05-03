# django_movies_project

# After clone project

cd django_movies_project

python -m venv venv

# venv MAC command

source venv/bin/activate

py -m pip install Django

cd mysite

python manage.py migrate

python manage.py runserver

# deactivate

deactivate

# run unit test

cd mysite/

python manage.py test movies

# after create new model(EX: Canvas)

cd mysite/

python manage.py makemigrations movies

python manage.py sqlmigrate movies 0003

python manage.py migrate

## Add these to movies/admin.py

from .models import Canvas
admin.site.register(Canvas)
