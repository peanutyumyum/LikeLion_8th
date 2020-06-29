from django.shortcuts import render
from .models import myAlbum
from django.shortcuts import render,get_object_or_404, redirect
from .forms import crateForm
from django.urls import reverse


# Create your views here.

def home(request):
    myAlbum_obj = myAlbum.object
    return render(request, 'home.html',{'myAlbum_obj':myAlbum_obj})

def add(request):
    form =crateForm()
    if request.method == "POST":
        add_obj = myAlbum()
        add_obj.name = request.POST['name']
        add_obj.artist = request.POST['artist']
        add_obj.release = request.POST['release']
        add_obj.playTime = request.POST['playTime']
        add_obj.genre = request.POST['genre']
        add_obj.albumArt = request.FILES['albumArt']
        add_obj.desription = request.POST['description']
        add_obj.save()
        return redirect('home')
    else:
        pass
    return render(request, 'add.html',{'form':form})

def change(request, change_id):
    change_obj = get_object_or_404(myAlbum, pk=change_id)
    form =crateForm()
    if request.method == "POST":
        myAlbum.name = request.POST['name']
        myAlbum.artist = request.POST['artist']
        myAlbum.release = request.POST['release']
        myAlbum.playTime = request.POST['playTime']
        myAlbum.genre = request.POST['genre']
        myAlbum.albumArt = request.FILES['albumArt']
        myAlbum.desription = request.POST['description']
        change_obj.save()
        return redirect(reverse('home'))
    else:
        pass
    return render(request,'change.html', {"change_key":change_obj,"form":form})

def delete(request, delete_id):
    delete_obj = get_object_or_404(myAlbum, pk=delete_id)
    delete_obj.delete()
    return redirect('home')
    