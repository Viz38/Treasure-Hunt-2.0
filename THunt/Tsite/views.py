from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentRegistrationForm,AnswerForm
from django.contrib.auth.decorators import login_required
from .models import Student,Answer
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def home(request):
    return HttpResponse("Hello, world.")


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentRegistrationForm()
        return render(request, 'users/register.html', {'form': form})
    # return render(request,'users/register',{'form':form})


def solution(request):

    try:
        user = Student.objects.get(usn = '4pa17cs000' )
    except Student.DoesNotExist:
        return messages.error("Usn not found")

    if request.method == 'POST':
        post_data = (request.POST)
        try:
            ans = Answer.objects.get(name = user)
            form = AnswerForm(post_data, instance=ans)
        except Answer.DoesNotExist:
            form = AnswerForm(post_data)

        if form.is_valid():
            ans = form.save(commit=False)
            ans.name = user
            ans.save()
            print(ans)
            return redirect('solution')
    else:
        try:
            ans = Answer.objects.get(name = user)
            form = AnswerForm(instance=ans)
        except Answer.DoesNotExist:
            form = AnswerForm()
        return render(request,'users/base.html',{'form':form})
