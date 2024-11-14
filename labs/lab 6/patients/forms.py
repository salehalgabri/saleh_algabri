from django import forms
from .models import Patients

# # الطريقة الثانية لإنشاء form
# class PatientsForm(forms.ModelForm):
#     first_name = forms.CharField(label="First Name", widget=forms.TextInput(), required=True, initial='patients', help_text="This Is The First Name")
#     second_name = forms.CharField(label="Second Name", widget=forms.TextInput(), required=True, initial='patients', help_text="This Is The Second Name")
#     age = forms.IntegerField(label="age", widget=forms.NumberInput(), required=True, initial=20)
#     image = forms.ImageField(label="Image", widget=forms.FileInput())
#     file_report = forms.FileField(label="file report", widget=forms.FileInput())
#     report = forms.CharField(label="report", widget=forms.Textarea())

#     class Meta:
#         model = Patients  # تأكد من أنك تستخدم النموذج المجيد
#         fields = ['first_name', 'second_name', 'age', 'image', 'file_report', 'report']


# طريقة لإنشاء form
class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients  # تحديد الـ model الذي سيتم العمل معه
        # fields = '__all__'  # إذا كنت تريد التعامل مع كل الحقول
        fields = ['first_name', 'last_name', 'age', 'report']  # تحديد الحقول التي نريد العمل معها
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'report': forms.Textarea(attrs={'class': 'form-control'}),
        }