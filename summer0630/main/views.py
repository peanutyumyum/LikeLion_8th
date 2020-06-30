from django.shortcuts import render
from .models import Orders, members, Goods, Sheets

# Create your views here.

def index(request):
    sheets_row = Sheets.objects.all()

    return render(request, 'index.html', {'sheets_row':sheets_row})

