from django.shortcuts import render
from apps.movies.models import Movie, Watch_List

def index(request):
    context = {
        'movies': Movie.objects.all(),
    }
    return render(request, 'movies/index.html', context)

def show(request, movie_id):
    context = {
        'movie': Movie.objects.get(id=movie_id),
    }
    return render(request, 'movies/show.html', context)

def watch_list(request):
    return render(request, 'movies/watch_list.html')
