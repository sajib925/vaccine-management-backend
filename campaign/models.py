from django.db import models
from doctor.models import Doctor

class CampaignModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.TextField(null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class VaccinesModel(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    schedule = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

