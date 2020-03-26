from django.forms import ModelForm
from .models import Student


class StudentRegistrationForm(ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'usn', 'year', 'branch']
