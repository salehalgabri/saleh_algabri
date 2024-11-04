from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Patients
from .forms import PatientsForm
import os
from django.db import IntegrityError
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request,'home.html')

def patients_home(request):
    return render(request,'patients_home.html')

def patients_list(request):
    patients=Patients.objects.all()
    if patients.exists:
        return render(request,'patients_list.html',{'patients':patients})

def message_success(request):
    return render(request,"patients/success_message.html")

def error_page(request):
    return render(request,"patients/error_page.html")

def patients_show_detail(request, pk):
    patient = get_object_or_404(Patients, id=pk)
    return render(request, 'patient_info.html', {"patient": patient})

# دالة حذف البيانات
def patient_delete(request, pk):
    try:
        patient = get_object_or_404(Patients, pk=pk)
        # حذف الصورة إذا كانت موجودة
        if patient.image:
            image_path = patient.image.path
            if os.path.isfile(image_path):
                os.remove(image_path)
                
        # حذف ملف التقرير إذا كان موجودًا
        if patient.file_report:
            file_report_path = patient.file_report.path
            if os.path.isfile(file_report_path):
                os.remove(file_report_path)
                
        # حذف المريض من قاعدة البيانات
        patient.delete()
        return redirect(reverse('patients:message_success'))
    except:
        return redirect(reverse('patients:error_page'))



# دالة إضافة البيانات
def patients_create(request):
    if request.method == 'POST':
        try:
            patient = Patients.objects.create(
                first_name=request.POST.get('fname'),
                last_name=request.POST.get('lname'),
                age=request.POST.get('age'),
                report=request.POST.get('report'),
                image=request.FILES.get('image'),
                file_report=request.FILES.get('medicalreport')
            )
            return redirect(reverse('patients:message_success'))
        except IntegrityError:
            return redirect(reverse('patients:error_page'))
    else:
        return render(request, 'patients_create.html')

# دالة تعديل البيانات
def patients_edit(request, pk):
    patient = get_object_or_404(Patients, id=pk)
    if request.method == 'POST':
        try:
            if patient.image:
                image_path = patient.image.path
                if os.path.isfile(image_path):
                    os.remove(image_path)
            patient.first_name = request.POST.get('fname')
            patient.last_name = request.POST.get('lname')
            patient.age = request.POST.get('age')
            patient.report = request.POST.get('report')
            patient.image = request.FILES.get('image')
            patient.file_report = request.FILES.get('medicalreport')
            patient.save()
            return redirect(reverse('patients:message_success'))
        except IntegrityError:
            return redirect(reverse('patients:error_page'))
    else:
        return render(request, 'patients_update.html', {'patient': patient})


def show_forms(request):
    if request.method == 'POST':
        patient_form = PatientsForm(request.POST, request.FILES)
        if patient_form.is_valid():
            patient_form.save()
            return HttpResponse('Created')
        else:
            return HttpResponse('Field!')
    else:
        patient_form = PatientsForm()
        return render(request, 'other_type_forms.html', {'form': patient_form})