from rest_framework import serializers
from datetime import timedelta
from .models import BookingModel


class BookingModelSerializer(serializers.ModelSerializer):
    # These fields are fetched from the related User model via the Patient model
    patient_id = serializers.ReadOnlyField(source='patient.user.id')
    patient_first_name = serializers.ReadOnlyField(source='patient.user.first_name')
    patient_last_name = serializers.ReadOnlyField(source='patient.user.last_name')
    campaign_name = serializers.ReadOnlyField(source='campaign.name')
    vaccine_name = serializers.ReadOnlyField(source='vaccine.name')

    class Meta:
        model = BookingModel
        fields = [
            'id', 'patient_id', 'patient_first_name', 'patient_last_name',
            'campaign', 'campaign_name', 'vaccine', 'vaccine_name',
            'first_dose_date', 'second_dose_date', 'created_at', 'updated_at'
        ]
        read_only_fields = ['second_dose_date']

    def create(self, validated_data):
        booking = BookingModel.objects.create(**validated_data)
        booking.second_dose_date = booking.first_dose_date + timedelta(days=28)
        booking.save()
        return booking


class BookingModelUpdateSerializer(serializers.ModelSerializer):
    # These fields are fetched from the related User model via the Patient model
    patient_id = serializers.ReadOnlyField(source='patient.user.id')
    campaign_name = serializers.ReadOnlyField(source='campaign.name')
    vaccine_name = serializers.ReadOnlyField(source='vaccine.name')

    class Meta:
        model = BookingModel
        fields = [
            'id', 'patient_id', 'campaign_name',  'vaccine_name', 'first_dose_date', 'second_dose_date',
        ]




