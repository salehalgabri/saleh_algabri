from django.urls import path
from . import views

urlpatterns = [
    path('',views.Employees_Page,name="Employees_Page"),
    path('Show_Employees/',views.Show_Employees,name='Show_Employees'),
    path('Edit_Employees/',views.Edit_Employees,name='Edit_Employees'),
    path('Delete_Employee/',views.Delete_Employee,name='Delete_Employee')
]
