from django.shortcuts import render, redirect
from . import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class PatientListCreateApiView(APIView):
    def get(self, request):
        patients = models.Patient.objects.all()
        serializer = serializers.PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Add the logged-in user to the request data
        request.data['user'] = request.user.id

        serializer = serializers.PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDetailApiView(APIView):
    def get(self, request, pk):
        patient = get_object_or_404(models.Patient, pk=pk)
        serializer = serializers.PatientSerializer(patient)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        patient = get_object_or_404(models.Patient, pk=pk)
        serializer = serializers.PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        patient = get_object_or_404(models.Patient, pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered and activated successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginApiView(APIView):
    serializer_class = serializers.UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
            else:
                return Response({'error': "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Ensure the user has an auth token and delete it
        try:
            request.user.auth_token.delete()
        except Token.DoesNotExist:
            return Response({"detail": "Token does not exist or already deleted."}, status=400)

        # Logout the user
        logout(request)
        return Response({"detail": "Successfully logged out."}, status=200)





class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = serializers.ProfileUpdateSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        serializer = serializers.ProfileUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class PasswordUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        serializer = serializers.PasswordUpdateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"detail": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         