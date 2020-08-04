from django.shortcuts import render, redirect
from .models import Jasoseol
from .forms import JssForm

# Create your views here.

def index(request):
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {"all_jss":all_jss})

def create(request):
    if request.method == "POST":
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')
    jss_form = JssForm()
    return render(request, 'create/html', {'jss_form':jss_form })

def detail(request):

    return render(request, 'detail.html')