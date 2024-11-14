from django.http import HttpResponse
from django.shortcuts import redirect
def isadmin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.exists():
            # تعيين نوع للمستخدم بعد إضافة بيانات لجمع groups
            group = request.user.groups.all()[0].name
            print(group)
            if group == 'admin':
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('401 Unauthorized')
        else:
            return HttpResponse('401 Unauthorized')
    return wrapper_func


def islogin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
