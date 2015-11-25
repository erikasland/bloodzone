from django.shortcuts import render
from apps.movies.models import Movie, Watch_List

def index(request):
    context = {
        'movies': Movie.objects.all(),
    }
    print context['movies']
    return render(request, 'movies/index.html', context)

def show(request):

    return render(request, 'movies/show.html')
