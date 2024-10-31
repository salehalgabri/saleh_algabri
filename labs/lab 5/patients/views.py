from django.shortcuts import render
from django.http import HttpResponse
from .models import Patients
# Create your views here.
def home(request):
    return render(request,'patients_home.html')
def patients_list(request):
    patients=Patients.objects.all()
    if patients.exists:
        return render(request,'patients_home.html',{'patients':patients})