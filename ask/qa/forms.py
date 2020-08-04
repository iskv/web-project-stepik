from django import forms
from .models import Question, Answer

from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        pass

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ChoiceField()

    def clean(self):     
        self.cleaned_data['question'] = Question.objects.get(pk=self.cleaned_data['question'])

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer





