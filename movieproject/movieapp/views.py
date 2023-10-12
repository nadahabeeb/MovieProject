from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from . models import movie
# Create your views here.
def home(request):
    movies=movie.objects.all()
    context={
        'movie_list':movies
    }
    return render(request,"index.html",context)
def detail(request,movie_id):
    mov=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':mov})

def add_movie(request):
    if request.method=='POST':
        name1=request.POST.get('name',)
        year1 = request.POST.get('year', )
        desc1 = request.POST.get('desc', )
        img1 = request.FILES['img']

        movieobj=movie(name=name1,year=year1,desc=desc1,img=img1)
        movieobj.save()

    return render(request,"add.html")

def update(request,id):
    movie1=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie1)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'movie':movie1,'form':form})

def delete(request,id):
    if request.method=='POST':
        movie1=movie.objects.get(id=id)
        movie1.delete()
        return redirect('/')
    return render(request,"delete.html")