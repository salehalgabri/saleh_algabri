from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
from django.db.models import Q
from .filters import StudentsFilter
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
    
    #------------filters----------------
    myFilter=StudentsFilter(request.GET,queryset=students)
    students=myFilter.qs
    
    return render(request,'Students/showstudents.html',{'students':students,'myFilter':myFilter})

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


def create_student(request):
    Students.objects.create(
    f_name='Ali',
    l_name='Mohammed',
    age=22,
    level="4",
    gpa=9.9,
    status=False,
    reporet="ss",
    ).save()
    return HttpResponse('Created')

def getStudents(request):
    # student=Students.objects.all()
    # student=Students.objects.filter(f_name__contains='o')#سيجلب البيانات التي تحتوي على حرف "o"
    # student=Students.objects.filter(gpa__in=[9.0])#سيجلب البيانات التي تحتوي على احد القيم في List
    # student=Students.objects.filter(gpa__range=[9.0,9.9])#سيجلب البيانات التي تكون في مدى في List
    # student=Students.objects.filter(gpa__exact=9.0)# سيجلب البيانات المحددة في العمود المحدد
    # student=Students.objects.all().exclude(f_name='Mohammed')#سيرجع بكل البيانات عدا الموجودة في الشرط
    student=Students.objects.all().exclude(Q(f_name='Mohammed')|Q(age=22))#سيرجع بكل البيانات عدا الموجودة في الشرط
    # student=Students.objects.all().order_by('gpa') #جلب البيانات تصاعدياً
    # student=Students.objects.all().order_by('-gpa')#جلب البيانات تنازلياً 
    # student=Students.objects.all()[0]
    count=Students.objects.all().count()
    return render(request,'showstudents.html',{'students':student})

def edit_students(request,pk): 
    student=Students.objects.get(pk=pk)
    student.level=4
    student.l_name='ALGABRI'
    student.gpa=8.0
    student.save()
    return HttpResponse("Update Done")

def delete_students(request,pk):
    student=Students.objects.get(pk=pk)
    student.delete()
    return HttpResponse("Delete Done")

