from django.shortcuts import render
from .models import *
from django.views.generic.base import View

# Create your views here.
class MoviesView(View):
    """Список фильмов"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movies_list.html", {'movies_list': movies})