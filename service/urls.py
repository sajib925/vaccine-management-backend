from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServiceAPIView.as_view(), name='service-list-create'),
]



