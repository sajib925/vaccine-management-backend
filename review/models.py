from django.conf import settings
from django.db import models
from campaign.models import CampaignModel
from patient.models import Patient

class CommentModel(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    campaign = models.ForeignKey(CampaignModel, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.patient} on {self.campaign.name}"
