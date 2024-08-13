from django.db import models
from datetime import timedelta
from campaign.models import CampaignModel, VaccinesModel
from patient.models import Patient


class BookingModel(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    campaign = models.ForeignKey(CampaignModel, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(VaccinesModel, on_delete=models.CASCADE)
    first_dose_date = models.DateField()
    second_dose_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.second_dose_date:
            self.second_dose_date = self.first_dose_date + timedelta(days=28)  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking for {self.patient} - {self.vaccine.name} on {self.first_dose_date}"