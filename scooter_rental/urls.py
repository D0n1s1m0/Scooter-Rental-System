from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("scooters/", include("scooters.urls")),
    path("rentals/", include("rentals.urls")),
]