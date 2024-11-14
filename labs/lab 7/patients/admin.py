from django.contrib import admin
from .models import Patients

# Register your models here.
admin.site.site_header="H.P.S"
admin.site.site_title="H.P.S"


class PatientsAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','age','image','report']  # أي البيانات تريد ظهورها على الجدول
    list_display_links=['first_name']  # أي الحقول التي يمكن الدخول منها كرابط
    list_editable=['last_name','age','report']  # أي الحقول التي تريد تعديلها من خارج الجدول بشرط أن لاتكون رابط
    search_fields=['first_name']  # البحث عن طريق إيش؟
    list_filter=['age']  # إظهار فلتر للأعمار
    fields=['first_name','last_name','age','image','report']  # أي الحقول التي تريد ان تظهر في الصفحة
admin.site.register(Patients, PatientsAdmin)
