from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from .decorators import islogin
# Create your views here.
def register(request):
    # هنا سنتحقق هل الفرم للمستخدم وتم إدخال بياناته وإرسالها
    if request.method == "POST":
        # نقوم بتعبيئة البيانات المرسلة في النموذج
        form = RegisterForm(request.POST)
        
        # نتحقق من صحة المدخلات
        if form.is_valid():
            # إذا كانت المدخلات صحيحة يتم حفظ البيانات
            form.save()
            user = form.cleaned_data.get('username')
            # يتم إرسال رسالة هنا بنجاح العملية
            messages.success(request, f"User {user} created successfully")
            # يتم إفهام فورد تسجيل الدخول
            return redirect('user:login')
        else:
            # إذا كان هناك مشكلة في الحقول يتم البناء على صفحة التسجيل والخطأ
            context = {'form': form}
            return render(request, 'register_form.html', context)
    else:
        # هنا نقوم بتسجيل النموذج الخاص بالمستخدم في ملف forms.py
        form = RegisterForm()
        context = {'form': form}
        # هنا نتوجه لصفحة التسجيل لإظهار النموذج
        return render(request, 'register_form.html', context)
    
@islogin
def userlogin(request):
    # التأكد من الطريقة POST وتهيئة النموذج بالبيانات
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        # التحقق من صحة البيانات المدخلة في النموذج
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            # محاولة الحصول على اسم المستخدم من البريد الإلكتروني
            try:
                username = User.objects.get(email=email).username
            except User.DoesNotExist:
                messages.error(request, "Invalid email or password")
                return redirect('user:login')
            
            # التحقق من المستخدم
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)  # بدء جلسة المستخدم
                return redirect('patients   :home')
            else:
                messages.error(request, "Invalid email or password")
                return redirect('user:login')
    else:
        # إذا كانت الطريقة GET، إنشاء نموذج فارغ
        form = LoginForm()

    # عرض نموذج تسجيل الدخول
    return render(request, 'login_form.html', {'form': form})


def userlogout(request):
    logout(request)
    return redirect("user:login")