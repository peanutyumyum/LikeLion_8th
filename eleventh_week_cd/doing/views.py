from django.shortcuts import render, redirect, get_object_or_404
from .models import Jasoseol
from .forms import JssForm
from django.http import Http404

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
    return render(request, 'create.html', {'jss_form':jss_form })

def detail(request, jss_id):
    try: # try는 일단 시도해봐라
        my_jss = Jasoseol.objects.get(pk=jss_id)
    except: # 예외의 경우에는
        raise Http404 # 404(에러)를 띄어라
    # or 
    # my_jss = get_object_or_404(Jasoseol, pk=jss_id)

    return render(request, 'detail.html', {'my_jss' : my_jss})



def update(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    jss_form = JssForm(instance=my_jss) # instance를 하기 전에는 비어있는 form의 형태이지만, instace를 사용함으로써 form안에 기존 db가 들어가서 표기가 되게 되었음
    if request.method == "POST":
        updated_form = JssForm(request.POST, isinstance=my_jss) # POST 방식으로 form 안에 넣겠다.
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index.html')

    return render(request, 'create.html', {'jss_form' : jss_form})

def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    my_jss.delete()
    return redirect('index.html')
