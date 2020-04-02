from django import forms
from .models import Student,Answer
from django.contrib.auth.forms import UserCreationForm


class StudentRegistrationForm(UserCreationForm):

    class Meta:
        model = Student
        fields = ['email', 'username', 'usn', 'year', 'branch']


# class AnswerForm(ModelForm):

#     class Meta:
#         model = Answer
#         fields = ['l1','l2','l3','l4','l5']

class SignInForm(forms.Form):

    email = forms.CharField(label="Your Email", max_length=100)
    password = forms.CharField(label="Your password", max_length=100,)