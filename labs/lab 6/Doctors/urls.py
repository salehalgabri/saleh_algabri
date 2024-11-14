from django.urls import path
from . import views

app_name = 'doctors'  # هذا السطر يعرّف الـ namespace الخاص بالتطبيق

urlpatterns = [
    path('', views.doctors_home, name='doctors_home'),
    path('show/', views.doctors_list, name='show'),
    path('update/<int:pk>/', views.doctors_edit, name='edit'),
    path('success/', views.success_message, name='success_message'),
    path('error/', views.error_page, name='error_page'),
    path('delete/<int:pk>/', views.doctors_delete, name='delete'),
    path('show/<int:pk>/', views.doctors_show_detail, name='showdetail'),  # تأكد من تصحيح اسم الدالة
    path('create/', views.doctors_create, name='create'),
    path('forms/', views.show_forms, name='forms'),
]
