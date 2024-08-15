from django.urls import path
from .views import BookingList, BookingAPIView

urlpatterns = [
    path('', BookingList.as_view(), name='booking-list'),
    path('<int:pk>/', BookingAPIView.as_view(), name='booking-delete'),
]
