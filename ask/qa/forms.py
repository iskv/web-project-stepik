from django import forms
from .models import Question, Answer

from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    author = forms.IntegerField() # placeholder

    def clean(self):
        self.cleaned_data['author'] = User(1) # placeholder

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.EmailField()
    author = forms.IntegerField() # placeholder

    def clean(self):
        self.cleaned_data['author'] = User(1) # placeholder
        self.cleaned_data['question'] = self.question_object # using property

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer





