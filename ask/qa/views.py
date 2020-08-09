from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.urls import reverse

from .paginator import paginator
from .models import Question
from .forms import AskForm, AnswerForm, UserCreationForm_custom
 
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
    all_questions = Question.objects.all()
    all_questions_with_pk = [(question.pk, question) for question in all_questions]

    if request.method == 'POST' and not request.user.is_authenticated:          
        return redirect(reverse('login') + '?next=%s' % request.path)
    
    if request.method == 'POST':       
        form = AnswerForm(request.POST, initial={'question': (question.pk, question)})
        form.fields['question'].choices = all_questions_with_pk                
        if form.is_valid():            
            form.save(request.user)
            url = question.get_url()
            return HttpResponseRedirect(url)    
    else:
        form = AnswerForm(initial={'question': (question.pk, question)})
        form.fields['question'].choices = all_questions_with_pk

    return render(request, 'qa/question.html', {        
        'question': question,
        'answers': answers,
        'form': form
    })

@login_required(login_url='login')
def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save(request.user)
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {
        'form': form
    })

def user_creation(request):
    if request.method == 'POST':        
        form = UserCreationForm_custom(request.POST)
        if form.is_valid():            
            user = form.save()
            login(request, user)
            return redirect('index')                    
    else:
        form = UserCreationForm_custom()    
    return render(request, 'qa/signup.html', {
        'form': form
    })


    