from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .paginator import paginator
from .models import Question
from .forms import AskForm, AnswerForm
 
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def index(request):
    new_posts = Question.objects.new()    
    index_paginator, page = paginator(request, new_posts)
    index_paginator.base_url = '?page='
    return render(request, 'qa/index.html', {
        'paginator': index_paginator,
        'page': page,
    }) 

def popular(request):
    popular_posts = Question.objects.popular()
    popular_paginator, page = paginator(request, popular_posts)
    popular_paginator.base_url = '?page='
    return render(request, 'qa/index.html', {
        'paginator': popular_paginator,
        'page': page
    }) 

def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answer_set.all()

    if request.method == 'POST':
        form = AnswerForm(request.POST, initial={'question': question.pk})         
        if form.is_valid():            
            form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()

    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {
        'form': form
    })