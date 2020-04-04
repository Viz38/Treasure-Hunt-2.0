from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentRegistrationForm, SignInForm
from django.contrib.auth.decorators import login_required
from .models import Student, Answer
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
    return render(request, 'users/index.html')


def home(request):
    return render(request, 'users/home.html')

def sign_in(request):
    
    if request.method == "POST":

        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            print(email)
            password = form.cleaned_data["password"]
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
                return redirect("level_1")
            else:
                return messages.error("User does not exist")
    form = SignInForm()
    return render(request, "users/signin.html", {'form': form})


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data["password1"]
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
                if request.GET.get('next'):
                  return redirect(request.GET['next'])  
                else:
                    return redirect("level_1")
        else:
            return render(request, 'users/home.html', {'form': form})
    form = StudentRegistrationForm()
    # Changed from register.html to home.html
    return render(request, 'users/home.html', {'form': form})
    # return render(request,'users/register',{'form':form})

@login_required(login_url='register')
def level_1(request):

    return render(request, "users/l1.html")

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
