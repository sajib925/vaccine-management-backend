from django.urls import path
from .views import CampaignList, VaccineList, VaccineDetail

urlpatterns = [
    path("", CampaignList.as_view(), name="campaign_list"),
    path("vaccine/", VaccineList.as_view(), name="vaccine_list"),
    path("<int:pk>/", VaccineDetail.as_view(), name="vaccine_detail"),
]
