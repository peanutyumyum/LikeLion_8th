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
        if filled_form.is_valid(): # is_valid 는 유효성 검사를 하는 함수이다. 문제가 없을 때 밑에 save 함수를 통해 저장함
            filled_form.save()
            return redirect('index')
    jss_form = JssForm()
    return render(request, 'create/html', {'jss_form':jss_form })

def detail(request):

    return render(request, 'detail.html')