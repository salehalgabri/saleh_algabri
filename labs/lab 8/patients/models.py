from django.db import models

# Create your models here.
class Patients(models.Model):
    first_name = models.CharField(max_length=30, default="Unknown")
    last_name = models.CharField(max_length=30, default="Unknown")
    age = models.PositiveIntegerField(default=18)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True)
    file_report = models.FileField(upload_to='files/%Y/%m/%d', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    report = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
