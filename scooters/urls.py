from django.urls import path

from . import views

urlpatterns = [
    path("", views.scooters, name="scooters"),
    path("<int:scooter_id>/", views.scooter_detail,
         name="scooter_detail"),
]