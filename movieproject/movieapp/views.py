from django.http import HttpResponse
from django.shortcuts import render, redirect
from movieapp.forms import moviesform
from movieapp.models import Movies


# Create your views here.
def index(request):
    movie=Movies.objects.all()
    value={
        'all_movies':movie
    }
    return render(request,'index.html',value)
# def detail(request,movie_id):
#     return HttpResponse("this is movie number %s" % movie_id)

def detail(request,movie_id):
    movie=Movies.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':movie})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        des=request.POST.get('des',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        movie=Movies(name=name,des=des,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request,'add.html')
def update(request, id,):
    movie=Movies.objects.get(id=id)
    form=moviesform(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')