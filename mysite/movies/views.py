from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.shortcuts import render
from .models import Movie
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
import random
from django.utils import timezone
from .models import Movie
from django.db.models import Q

def index(request):
    latest_question_list = Movie.objects.order_by("id")
    context = {"latest_question_list": latest_question_list}
    return render(request, "movies/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Movie, pk=question_id)
    return render(request, "movies/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def createpoll(request):
    return render(request, "movies/createpoll.html", {})

def submitpoll(request):
    if request.method == "POST":
        question_text = request.POST["question_text"]
        choice1_text = request.POST["choice1"]
        choice2_text = request.POST["choice2"]

        question = Movie(title=question_text, star=choice1_text, desc=choice2_text)

        question.save()

        # question.choice_set.create(choice_text=choice1_text, votes=0)
        # question.choice_set.create(choice_text=choice2_text, votes=0)


    latest_question_list = Movie.objects.order_by("id")
    context = {"latest_question_list": latest_question_list}
    return render(request, "movies/index.html", context)

def edit(request, question_id):
    question = get_object_or_404(Movie, pk=question_id)
    # return render(request, "movies/detail.html", {"question": question})
    return render(request, "movies/edit.html", {"question":question})

def submitedit(request, question_id):
    if request.method == "POST":
        question = get_object_or_404(Movie, pk=question_id)
        question.title = request.POST["question_text"]
        question.star = request.POST["choice1"]
        question.desc = request.POST["choice2"]
        question.save()

    latest_question_list = Movie.objects.order_by("id")
    context = {"latest_question_list": latest_question_list}

    return render(request, "movies/index.html", context)

def delete(request, question_id):
    q = Movie.objects.get(pk=question_id)
    q.delete()
    latest_question_list = Movie.objects.order_by("id")
    context = {"latest_question_list": latest_question_list}
    return render(request, "movies/index.html", context)

def last_question(request):
    latest_movie = Movie.objects.latest("id")
    context = {"last_one": latest_movie}
    return render(request, "movies/last_question.html", context)

def magic_missile(request, my_name):
    context = {"my_name": my_name}
    return render(request, "movies/magic_missile.html", context)

def my_position(request, my_position):
    context = {"my_position": my_position + 1000}
    return render(request, "movies/magic_missile.html", context)


def search(request):
    keyword = request.POST["keyword"]
    print("keyword="+keyword)
    if keyword:
        search_result = Movie.objects.filter(Q(title__icontains=keyword))
        print(search_result)
    else:
        search_result = Movie.objects.all()

    context = {"keyword": keyword, "search_result": search_result}
    return render(request, "movies/index.html", context)