from django.db import models

# Create your models here.
class Doctors(models.Model):
    first_name = models.CharField(max_length=30, default="Unknown")
    last_name = models.CharField(max_length=30, default="Unknown")
    age = models.PositiveIntegerField(default=18)
    Specialization=models.CharField(max_length=50,default="Unknown")
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"