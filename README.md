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
