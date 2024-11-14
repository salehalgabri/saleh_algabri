from django import forms
from .models import Doctors


class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors  # تحديد الـ model الذي سيتم العمل معه
        # fields = '__all__'  # إذا كنت تريد التعامل مع كل الحقول
        fields = ['first_name', 'last_name', 'age', 'Specialization']  # تحديد الحقول التي نريد العمل معها
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'Specialization': forms.TextInput(attrs={'class': 'form-control'}),
        }