from django.forms import ModelForm
from .models import Student,Answer


class StudentRegistrationForm(ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'usn', 'year', 'branch']


class AnswerForm(ModelForm):

    class Meta:
        model = Answer
        fields = ['l1','l2','l3','l4','l5']