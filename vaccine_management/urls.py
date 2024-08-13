from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include("doctor.urls")),
    path('api/auth/', include("patient.urls")),
    path('api/contact/', include("contact_us.urls")),
    path('api/service/', include("service.urls")),
    path('api/booking/', include("booking.urls")),
    path('api/review/', include("review.urls")),
    path('api/campaign/', include("campaign.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
