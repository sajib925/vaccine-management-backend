from django.contrib import admin
from .models import CampaignModel, VaccinesModel
# Register your models here.

admin.site.register(CampaignModel)
admin.site.register(VaccinesModel)
