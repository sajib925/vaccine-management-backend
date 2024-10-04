from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=250, blank=True, null=True)
    mobile_no = models.CharField(max_length=12)
    nid = models.CharField(max_length=12, unique=True)
    age = models.CharField(max_length=5)
    medical_info = models.TextField(blank=True, null=True)

    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"