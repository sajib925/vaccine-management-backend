from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from . import models, serializers

class DoctorListCreateApiView(APIView):
    def get(self, request):
        doctors = models.Doctor.objects.all()
        serializer = serializers.DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.DoctorSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorDetailApiView(APIView):
    def get(self, request, pk):
        doctor = get_object_or_404(models.Doctor, pk=pk)
        serializer = serializers.DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk):
        doctor = get_object_or_404(models.Doctor, pk=pk)
        serializer = serializers.DoctorSerializer(doctor, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        doctor = get_object_or_404(models.Doctor, pk=pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
