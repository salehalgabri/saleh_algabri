from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import SignUpForm
# Create your views here.
def signup(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)    
            return redirect('index')
    return render(request,'signup.html',{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('index')