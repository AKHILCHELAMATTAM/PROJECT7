from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.shortcuts import render

# Create your views here.
def fun7(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, "amal.html",context)
#def details(request,movie_id):
#   return HttpResponse("this is",%movie_id)
def fundetails(request, movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request, "don.html",{'movie':movie})