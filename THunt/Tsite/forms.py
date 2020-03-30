from django import forms
from .models import Student,Answer


class StudentRegistrationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'usn', 'year', 'branch']


# class AnswerForm(ModelForm):

#     class Meta:
#         model = Answer
#         fields = ['l1','l2','l3','l4','l5']

class SignInForm(forms.Form):

    name = forms.CharField(label="Your Name", max_length=100)
    usn = forms.CharField(label="Your usn", max_length=100)