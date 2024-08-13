from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServiceListCreateApiView.as_view(), name='service-list-create'),
]
