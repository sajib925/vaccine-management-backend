from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers

class ServiceAPIView(APIView):
    def get(self, request, *args, **kwargs):
        services = models.Service.objects.all()
        serializer = serializers.ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
