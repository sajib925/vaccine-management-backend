from django.db import models
from campaign.models import CampaignModel
from patient.models import Patient


STAR_CHOICES = [
    ('1', '⭐'),
    ('2', '⭐⭐'),
    ('3', '⭐⭐⭐'),
    ('4', '⭐⭐⭐⭐'),
    ('5', '⭐⭐⭐⭐⭐'),
]
class CommentModel(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    campaign = models.ForeignKey(CampaignModel, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.CharField(choices=STAR_CHOICES, max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.patient} on {self.campaign.name}"
