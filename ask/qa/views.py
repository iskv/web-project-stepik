from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .paginator import paginator
from .models import Question
 
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
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers
    })