from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentRegistrationForm
from django.contrib.auth.decorators import login_required
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
