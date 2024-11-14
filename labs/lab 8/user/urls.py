from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.userlogin, name='login'),
    path('register/', views.register, name='register'),
    path('logout/   ', views.userlogout, name='logout'),
]