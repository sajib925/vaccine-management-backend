from django.urls import path
from . import views

urlpatterns = [
    path('doctor/', views.DoctorListCreateApiView.as_view(), name='doctor-list-create'),
    path('doctor/<int:pk>/', views.DoctorDetailApiView.as_view(), name='doctor-detail'),
]
