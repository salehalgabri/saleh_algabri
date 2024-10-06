from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('showstudents',views.showstudents,name="show"),
    path('editstudents',views.editstudents,name="edit"),
    path('deletestudents',views.deletestudents,name="delete"),
    
]