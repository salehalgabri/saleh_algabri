from django.urls import path
from . import views

app_name = 'patients'  # هذا السطر يعرّف الـ namespace الخاص بالتطبيق

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patients_home, name='patients_home'),
    path('create/', views.patients_create, name='create'),
    path('show/', views.patients_list, name='show'),
    path('success/', views.message_success, name='message_success'),
    path('error/', views.error_page, name='error_page'),
    path('show/<int:pk>/', views.patients_show_detail, name='showdetail'),  # تأكد من تصحيح اسم الدالة
    path('update/<int:pk>/', views.patients_edit, name='edit'),
    path('delete/<int:pk>/', views.patient_delete, name='delete'),
    path('forms/', views.show_forms, name='forms'),
]
