from rest_framework import serializers
from .models import CampaignModel, VaccinesModel



class CampaignModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignModel
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class VaccinesModelSerializer(serializers.ModelSerializer):
    doctor_username = serializers.ReadOnlyField(source='doctor.username')
    class Meta:
        model = VaccinesModel
        fields = ['id','doctor_username', 'name', 'schedule' ]



