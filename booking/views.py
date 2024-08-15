from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import BookingModel
from .serializers import BookingModelSerializer, BookingModelUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from django.http import Http404

class BookingList(APIView):
    def get(self, request, format=None):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Filter bookings by the logged-in user's patient profile
        try:
            patient = request.user.patient
        except AttributeError:
            return Response({"detail": "Only patients can view bookings."}, status=status.HTTP_403_FORBIDDEN)

        bookings = BookingModel.objects.filter(patient=patient)
        serializer = BookingModelSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if not request.user.is_authenticated or not hasattr(request.user, 'patient'):
            return Response({"detail": "Only authenticated patients can make bookings."},
                            status=status.HTTP_403_FORBIDDEN)

        patient = request.user.patient
        serializer = BookingModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(patient=patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BookingAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return BookingModel.objects.get(pk=pk)
        except BookingModel.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):

        if not hasattr(request.user, 'patient'):
            return Response({"detail": "Only patient can update booking."}, status=status.HTTP_403_FORBIDDEN)

        booking = self.get_object(pk)
        serializer = BookingModelUpdateSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):

        if not hasattr(request.user, 'patient'):
            return Response({"detail": "Only patient can delete booking."}, status=status.HTTP_403_FORBIDDEN)

        booking = self.get_object(pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)