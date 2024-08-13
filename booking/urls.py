from django.urls import path
from .views import BookingList

urlpatterns = [
    path('', BookingList.as_view(), name='booking-list'),
]
