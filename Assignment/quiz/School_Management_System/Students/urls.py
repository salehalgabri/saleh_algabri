from django.urls import path
from . import views

urlpatterns = [
    path('',views.Students,name='Students')
]
