from rest_framework import serializers
from .models import Doctors

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = "__all__"
        # fields = ['first_name', 'email', 'last_name']