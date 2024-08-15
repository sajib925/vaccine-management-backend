from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CampaignModel, VaccinesModel
from .serializers import CampaignModelSerializer, VaccinesModelSerializer
from rest_framework.permissions import IsAuthenticated

class CampaignList(APIView):

    def get(self, request, format=None):
        campaigns = CampaignModel.objects.all()
        serializer = CampaignModelSerializer(campaigns, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if not hasattr(request.user, 'doctor'):
            return Response({"detail": "Only doctors can create vaccines."}, status=status.HTTP_403_FORBIDDEN)

        doctor = request.user.doctor
        serializer = CampaignModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(doctor=doctor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class VaccineList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        vaccines = VaccinesModel.objects.all()
        serializer = VaccinesModelSerializer(vaccines, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Check if the user is a doctor
        if not hasattr(request.user, 'doctor'):
            return Response({"detail": "Only doctors can create vaccines."}, status=status.HTTP_403_FORBIDDEN)

        # Assign the logged-in doctor to the vaccine
        doctor = request.user.doctor
        serializer = VaccinesModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(doctor=doctor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VaccineDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return VaccinesModel.objects.get(pk=pk)
        except VaccinesModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vaccine = self.get_object(pk)
        serializer = VaccinesModelSerializer(vaccine)
        return Response(serializer.data)

    def put(self, request, pk, format=None):

        if not hasattr(request.user, 'doctor'):
            return Response({"detail": "Only doctors can delete vaccines."}, status=status.HTTP_403_FORBIDDEN)

        vaccine = self.get_object(pk)
        serializer = VaccinesModelSerializer(vaccine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):

        if not hasattr(request.user, 'doctor'):
            return Response({"detail": "Only doctors can delete vaccines."}, status=status.HTTP_403_FORBIDDEN)
        
        vaccine = self.get_object(pk)
        vaccine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)