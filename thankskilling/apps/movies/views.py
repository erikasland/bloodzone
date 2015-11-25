from django.shortcuts import render, redirect
from apps.movies.models import Movie, Watch_List
from apps.myauth.models import User

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
    user_list = Watch_List.objects.filter(user=request.session['id'])
    context = {
        'user_list' : user_list,
    }
    return render(request, 'movies/watch_list.html', context)

def add_to_list(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    user = User.objects.get(id=request.session['id'])
    Watch_List.objects.create(movie=movie, user=user)
    return redirect('watch_list')

def remove(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    user = User.objects.get(id=request.session['id'])
    WL_id = Watch_List.objects.filter(movie=movie, user=user)[0].id
    Watch_List.objects.get(id=WL_id).delete()
    return redirect('watch_list')
