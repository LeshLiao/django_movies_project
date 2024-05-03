from django.urls import path

from . import views

app_name = "movies"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

    path("createpoll/", views.createpoll, name="createpoll"),
    path("submitpoll/", views.submitpoll, name="submitpoll"),
    path("submitedit/<int:question_id>/", views.submitedit, name="submitedit"),
    path("delete/<int:question_id>/", views.delete, name="delete"),
    path("<int:question_id>/edit/", views.edit, name="edit"),

    path("last_question/", views.last_question, name="last_question"),

    path("magic_missile/<str:my_name>/", views.magic_missile, name="magic_missile"),

    path("position/<int:my_position>/", views.my_position, name="my_position"),

    path("search/", views.search, name="search"),
    path("change_color/", views.change_color, name="change_color"),
]