# from rest_framework import serializers
# from .models import Service
#
# class ServiceSerializer(serializers.ModelSerializer):
#     image_url = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Service
#         fields = ['id', 'image_url', 'name', 'description']
#
#     def get_image_url(self, obj):
#         request = self.context.get('request', None)
#         if request:
#             return request.build_absolute_uri(obj.image.url)
#         return obj.image.url
#
#


from rest_framework import serializers
from . import models

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'