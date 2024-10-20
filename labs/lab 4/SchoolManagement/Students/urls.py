from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('showstudents/',views.showstudents,name="show"),
    path('editstudents/',views.editstudents,name="edit"),
    path('deletestudents/',views.deletestudents,name="delete"),
    path('createNewStudent/',views.create_student,name="create"),
    path('getStudents/',views.getStudents,name="getStudent"),
    path('edit_students/<int:pk>',views.edit_students,name="edit_students"),
    path('delete_students/<int:pk>',views.delete_students,name="delete_students"),
]