from django.urls import path
from . import views

urlpatterns = [
    path('patient/', views.PatientListCreateApiView.as_view(), name='patient-list-create'),
    path('patient/<int:pk>/', views.PatientDetailApiView.as_view(), name='patient-detail'),
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('password/', views.PasswordUpdateView.as_view(), name='password-update'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]





















