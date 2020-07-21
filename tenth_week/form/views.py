from django.shortcuts import render
from .forms import Firstform, SecondForm

# Create your views here.

def index(request):
    form = Firstform()
    form2 = SecondForm()
    return render(request, 'index.html', {'form' : form}, {'form2': form2})



