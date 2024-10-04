# from rest_framework import serializers
# from .models import CommentModel
#
# class CommentModelSerializer(serializers.ModelSerializer):
#     patient_first_name = serializers.SerializerMethodField()
#     patient_last_name = serializers.SerializerMethodField()
#     campaign_name = serializers.ReadOnlyField(source='campaign.name')
#
#     class Meta:
#         model = CommentModel
#         fields = ['id', 'patient_first_name', 'patient_last_name', 'campaign', 'campaign_name', 'comment', 'created_at', 'updated_at']
#
#     def get_patient_first_name(self, obj):
#         return obj.patient.user.first_name if obj.patient and obj.patient.user else None
#
#     def get_patient_last_name(self, obj):
#         return obj.patient.user.last_name if obj.patient and obj.patient.user else None
#
#


from rest_framework import serializers
from .models import CommentModel

class CommentModelSerializer(serializers.ModelSerializer):
    patient_first_name = serializers.SerializerMethodField()
    patient_last_name = serializers.SerializerMethodField()
    campaign_name = serializers.ReadOnlyField(source='campaign.name')

    class Meta:
        model = CommentModel
        fields = ['id', 'patient_first_name', 'patient_last_name', 'campaign', 'campaign_name', 'comment', 'rating', 'created_at', 'updated_at']

    def get_patient_first_name(self, obj):
        return obj.patient.user.first_name if obj.patient and obj.patient.user else None

    def get_patient_last_name(self, obj):
        return obj.patient.user.last_name if obj.patient and obj.patient.user else None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        rating_value = instance.rating
        rating_star_map = {
            '1': '⭐',
            '2': '⭐⭐',
            '3': '⭐⭐⭐',
            '4': '⭐⭐⭐⭐',
            '5': '⭐⭐⭐⭐⭐',
        }
        representation['rating'] = rating_star_map.get(rating_value, rating_value)
        return representation

    def to_internal_value(self, data):
        rating_map = {
            '⭐': '1',
            '⭐⭐': '2',
            '⭐⭐⭐': '3',
            '⭐⭐⭐⭐': '4',
            '⭐⭐⭐⭐⭐': '5',
        }
        rating_symbol = data.get('rating')
        data['rating'] = rating_map.get(rating_symbol, rating_symbol)
        return super().to_internal_value(data)
