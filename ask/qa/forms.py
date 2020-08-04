from django import forms
from .models import Question, Answer

from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        #self.cleaned_data['author'] = User(1)
        pass

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        all_questions = Question.objects.all()
        all_questions_with_pk = [(question.pk, question) for question in all_questions]
        self.fields.get('question').choices = all_questions_with_pk

    def clean(self):
        #self.cleaned_data['author'] = User(1) # placeholder
        print(self.cleaned_data)
        self.cleaned_data['question'] = Question.objects.get(pk=self.cleaned_data['question'])

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer





