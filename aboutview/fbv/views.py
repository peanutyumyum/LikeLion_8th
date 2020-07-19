from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question
from django.urls import reverse

# Create your views here.

def index(request):
    # question_row = Qusetion.objects.all().order_by('-pub_date'
    objects = Question.objects.all()
    latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    #0~4개 까지 -(내림차순)으로 가져오겠다
    return render(request, 'fbv/index.html', {'latest_question_list': latest_question_list, 'ob':objects})
    # render(보낼방식, 보낼곳, 보낼내용)
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question':question
    }
    return render(request, 'fbv/detail.html', context)
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'fbv/result.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST)
    except (KeyError, Choice.DoesNotExit):
        return render(request, 'fbv/detail.html',
        {'question' : question, 'error_msg':"you dudn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('fbv:results', args=(question.id,)))
    
    return render(request, 'fbv/result.html')
