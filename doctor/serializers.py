from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class DoctorSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = models.Doctor
        fields = '__all__'

