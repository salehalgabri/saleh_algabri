from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def Home(request):
    return render(request,'Home/Home.html')

