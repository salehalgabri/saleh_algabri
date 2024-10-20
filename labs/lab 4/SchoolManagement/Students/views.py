from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
# Create your views here.
def index(request):
    name={
        'fname':'malek',
    }
    return render(request,'Students/index.html',name)

def home(request):
    return render(request,'Students/home.html')

def showstudents(request):
    # students = {
    #     "name":"Malek",
    #     "marks":[90,95,98,97],
    #     "eachsub":{
    #         "Software Engineering":96,
    #         "Image Processing":94,
    #         "Client and Server Programming":96
    #         },
    # }
    students=Students.objects.all()
    return render(request,'Students/showstudents.html',{'students':students})

def editstudents(request):
    students={
        'total':286,
        'marks':{
            "Software Engineering":96,
            "Image Processing":94,
            "Client and Server Programming":96
            }
    }
    return render(request,'Students/editstudents.html',students)

def deletestudents(request):
    return render(request,'Students/deletestudents.html')

# def

def create_student(request):
    Students.objects.create(
    f_name='Mohammed',
    l_name='Alhosany',
    age=22,
    level="4",
    gpa=9.9,
    status=False,
    reporet="ss",
    ).save()
    return HttpResponse('Created')