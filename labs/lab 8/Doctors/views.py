from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.db import IntegrityError
from .models import Doctors
from django.contrib.auth.decorators import login_required
from .forms import DoctorsForm
import os
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import DoctorSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
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


@api_view(["GET", "POST"])
def doctor_list(request):
    if request.method == "GET":
        try:
            doctors = Doctors.objects.all()
            serializer = DoctorSerializer(doctors, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": f"An error while retrieving doctors list: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    
    elif request.method == "POST":
        try:
            serializer = DoctorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Data added successfully",
                        "status": status.HTTP_201_CREATED,
                    },
                    status=status.HTTP_201_CREATED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": f"An error while saving the doctor: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

@api_view(["GET", "PUT", "DELETE"])
def doctor_detail(request, doctor_id):
    try:
        doctor = get_object_or_404(Doctors, id=doctor_id)
    except Exception as e:
        return Response(
            {"error": f"Doctor not found: {str(e)}"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        try:
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": f"An error while retrieving doctor data: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    elif request.method == "PUT":
        try:
            serializer = DoctorSerializer(doctor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": f"An error while updating doctor data: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    elif request.method == "DELETE":
        try:
            doctor.delete()
            return Response(
                {"message": "Doctor deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as e:
            return Response(
                {"error": f"An error while deleting doctor data: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
