from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    # The user is automatically set in the view, so exclude it from the input fields
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        doctor = Doctor.objects.create(user=user, **validated_data)
        return doctor
