from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

# Create your views here.

def signup(request):
    regi_form = UserCreationForm()
    if request.method == "POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')
    return render(request, 'signup.html', {'regi_form' : regi_form})

class MyLoginView(LoginView):
    template_name = 'login.html' # Django의 기본 제공 기능인 LoginView를 상속한 다음 커스터마이징 하였다.