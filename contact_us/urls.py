from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsListCreateApiView.as_view(), name='contactus-list-create'),
]
