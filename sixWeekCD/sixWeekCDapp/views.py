from django.shortcuts import render
from .models import youTubeChannel
from django.shortcuts import render,get_object_or_404, redirect
from .forms import crateForm

# Create your views here.

def home(request):
    youtube = youTubeChannel.objects
    return render(request, 'home.html',{'youtube':youtube})

def detail(request,detail_id):
    detail = get_object_or_404(youTubeChannel, pk=detail_id)
    return render(request, 'detail.html', {'youtube':detail})

def create(request):
    youtube = youTubeChannel()
    youtube.name = request.POST['name']
    youtube.creator = request.POST['creator']
    youtube.subscribers = request.POST['subscribers']
    youtube.preference = request.POST['preference']
    youtube.link1 = request.POST['link1']
    youtube.link2 = request.POST['link2']
    youtube.link3 = request.POST['link3']
    youtube.summary = request.POST['summary']
    youtube.text = request.POST['text']
    youtube.live = request.POST['live']
    youtube.photo = request.POST['photo']
    youtube.save()
    return redirect('home')

def new(request):
    form =crateForm()
    if request.method =='POST':
        pass
    elif request.method == 'GET':
        form = crateForm()
        return render(request, 'new.html',{'form':form})
    else:
        pass
    


