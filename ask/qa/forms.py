from django import forms
from .models import Question, Answer

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def save(self, user_obj):
        self.cleaned_data['author'] = user_obj
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ChoiceField()

    def clean(self):
        # for stepik start
        if self.data.get('question_id'):
            self.cleaned_data['question'] = self.data.get('question_id')
        # for stepik stop           
        self.cleaned_data['question'] = Question.objects.get(pk=self.cleaned_data['question'])

    def save(self, user_obj):
        self.cleaned_data['author'] = user_obj
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class UserCreationForm_custom(UserCreationForm):
    password1 = password2 = None

    def save(self, commit=True):
        user = forms.ModelForm.save(self, commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    

    class Meta(UserCreationForm.Meta):                
        fields = UserCreationForm.Meta.fields + ("password", "email")
        widgets = {
        'password': forms.PasswordInput(),
        }


    

    

        




