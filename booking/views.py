# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import BookingModel
# from .serializers import BookingModelSerializer
#
# class BookingList(APIView):
#     def get(self, request, format=None):
#         bookings = BookingModel.objects.all()
#         serializer = BookingModelSerializer(bookings, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#
#         if not hasattr(request.user, 'patient'):
#             return Response({"detail": "Only patients can make bookings.."}, status=status.HTTP_403_FORBIDDEN)
#
#         patient = request.user.patient
#         serializer = BookingModelSerializer(data=request.data)
#         serializer.patient = request.user
#         if serializer.is_valid():
#             serializer.save(patient=patient)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#


from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import BookingModel
from .serializers import BookingModelSerializer


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

