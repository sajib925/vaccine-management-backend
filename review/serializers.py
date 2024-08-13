# from rest_framework import serializers
# from .models import CommentModel
# from django.contrib.auth.models import User

# class CommentModelSerializer(serializers.ModelSerializer):
#     # patient_username = serializers.ReadOnlyField(source='patient.username')
#     patient_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     campaign_name = serializers.ReadOnlyField(source='campaign.name')
#
#     class Meta:
#         model = CommentModel
#         fields = ['id', 'patient_id', 'campaign', 'campaign_name', 'comment', 'created_at', 'updated_at']


from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CommentModel

class CommentModelSerializer(serializers.ModelSerializer):
    patient_first_name = serializers.SerializerMethodField()
    patient_last_name = serializers.SerializerMethodField()
    campaign_name = serializers.ReadOnlyField(source='campaign.name')

    class Meta:
        model = CommentModel
        fields = ['id', 'patient_first_name', 'patient_last_name', 'campaign', 'campaign_name', 'comment', 'created_at', 'updated_at']

    def get_patient_first_name(self, obj):
        return obj.patient.user.first_name if obj.patient and obj.patient.user else None

    def get_patient_last_name(self, obj):
        return obj.patient.user.last_name if obj.patient and obj.patient.user else None


