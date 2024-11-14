from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.db import IntegrityError
from .models import Doctors
from django.contrib.auth.decorators import login_required
from .forms import DoctorsForm
import os
# Create your views here.
@login_required(login_url="user:login")
def doctors_home(request):
    return render(request,"doctors_home.html")
@login_required(login_url="user:login")
def doctors_list(request):
    doctors=Doctors.objects.all()
    if doctors.exists:
        return render(request,"doctors_lits.html",{'doctors':doctors})
    
@login_required(login_url="user:login")
def doctors_edit(request, pk):
    doctor = get_object_or_404(Doctors, id=pk)
    if request.method == 'POST':
        try:
            if doctor.image:
                image_path = doctor.image.path
                if os.path.isfile(image_path):
                    os.remove(image_path)
            doctor.first_name = request.POST.get('fname')
            doctor.last_name = request.POST.get('lname')
            doctor.age = request.POST.get('age')
            doctor.Specialization = request.POST.get('Specialization')
            doctor.image = request.FILES.get('image')
            doctor.save()
            return redirect(reverse('doctors:success_message'))
        except IntegrityError:
            return redirect(reverse('doctors:error_page'))
    else:
        return render(request, 'doctors_update.html', {'doctor': doctor})

@login_required(login_url="user:login")
def doctors_delete(request, pk):
    try:
        doctor = get_object_or_404(Doctors, pk=pk)
        # حذف الصورة إذا كانت موجودة
        if doctor.image:
            image_path = doctor.image.path
            if os.path.isfile(image_path):
                os.remove(image_path)
        doctor.delete()
        return redirect(reverse('doctors:success_message'))
    except:
        return redirect(reverse('doctors:error_page'))

@login_required(login_url="user:login")
def doctors_show_detail(request, pk):
    doctor = get_object_or_404(Doctors, id=pk)
    return render(request, 'doctors_info.html', {"doctor": doctor})
@login_required(login_url="user:login")
def doctors_create(request):
    if request.method == 'POST':
        try:
            doctor = Doctors.objects.create(
                first_name=request.POST.get('fname'),
                last_name=request.POST.get('lname'),
                age=request.POST.get('age'),
                Specialization=request.POST.get('Specialization'),
                image=request.FILES.get('image'),
            )
            return redirect(reverse('doctors:success_message'))
        except IntegrityError:
            return redirect(reverse('doctors:error_page'))
    else:
        return render(request, 'doctors_create.html')


def success_message(request):
    return render(request,"doctors/success_message.html")

def error_page(request):
    return render(request,"doctors/error_page.html")
@login_required(login_url="user:login")
def show_forms(request):
    if request.method == 'POST':
        doctor_form = DoctorsForm(request.POST)
        if doctor_form.is_valid():
            doctor_form.save()
            return HttpResponse('Created')
        else:
            return HttpResponse('Field!')
    else:
        doctor_form = DoctorsForm()
        return render(request, 'doctors_forms.html', {'form': doctor_form})
