from django.shortcuts import render,redirect
from .models import singer
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.

def home(request):
    singer_obj = singer.object
    return render(request,'home.html',{'home_key' : singer_obj})

def detail(request, detail_id):
    detail_obj = get_object_or_404(singer, pk=detail_id)
    return render(request, 'detail.html', {'detail_key' : detail_obj})

def add(request):
    if request.method == "POST":
        singer_val = singer()
        singer_val.singerName = request.POST['nameSinger']
        singer_val.favSongName1 = request.POST['favSong1']
        singer_val.whyFavSinger = request.POST['why']
        singer_val.save()
        return redirect('home')
    else:
        pass
    return render(request, 'add.html')

def change(request, change_id):
    change_obj = get_object_or_404(singer, pk=change_id)
    if request.method == "POST":
        change_obj.singerName = request.POST['nameSinger']
        change_obj.favSongName1 = request.POST['favSong1']
        change_obj.whyFavSinger = request.POST['why']
        change_obj.save()
        return redirect(reverse('detail', args=(change_id)))
    else:
        pass
    return render(request,'change.html', {"change_key":change_obj})

def delete(request, delete_id):
    delete_obj = get_object_or_404(singer, pk=delete_id)
    delete_obj.delete()
    return redirect('home')