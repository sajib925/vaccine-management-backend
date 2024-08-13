from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers

class ContactUsListCreateApiView(APIView):
    def get(self, request):
        contacts = models.ContactUs.objects.all()
        serializer = serializers.ContactUsSerializer(contacts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



