from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentRegistrationForm, SignInForm
from django.contrib.auth.decorators import login_required
from .models import Student, Answer
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def index(request):
    return render(request, 'users/index.html')


def home(request):
    return render(request, 'users/home.html')

def sign_in(request):
    
    if request.method == "POST":

        form = SignInForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            usn = form.cleaned_data['usn']
            try:
                student = Student.objects.get(usn=usn, name=name)
                request.session["name"] = student.name
                request.session["usn"] = student.usn
                return redirect("level_1")
            except Student.DoesNotExist:
                return redirect("register")
    else:
        form = SignInForm()
        return render(request, "users/signin.html", {'form': form})


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = StudentRegistrationForm()
    else:
        form = StudentRegistrationForm()
        return render(request, 'users/register.html', {'form': form})
    # return render(request,'users/register',{'form':form})


def level_1(request):

    if request.session["usn"]:
        return render(request, "users/l1.html")
    else:
        return messages.error("Usn not found")

# def solution(request):

#     try:
#         user = Student.objects.get(usn = '4pa17cs000' )
#     except Student.DoesNotExist:
#         return messages.error("Usn not found")

#     if request.method == 'POST':
#         post_data = (request.POST)
#         try:
#             ans = Answer.objects.get(name = user)
#             form = AnswerForm(post_data, instance=ans)
#         except Answer.DoesNotExist:
#             form = AnswerForm(post_data)

#         if form.is_valid():
#             ans = form.save(commit=False)
#             ans.name = user
#             ans.save()
#             print(ans)
#             return redirect('solution')
#     else:
#         try:
#             ans = Answer.objects.get(name = user)
#             form = AnswerForm(instance=ans)
#         except Answer.DoesNotExist:
#             form = AnswerForm()
#         return render(request,'users/base.html',{'form':form})
