from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers

class ServiceListCreateApiView(APIView):
    def get(self, request):
        services = models.Service.objects.all()
        serializer = serializers.ServiceSerializer(services, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ServiceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
