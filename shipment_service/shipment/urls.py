from .views import ShipmentAPIView, ShipmentOfUserAPIView
from django.urls import path

urlpatterns = [
    path('add/', ShipmentAPIView.as_view()),
    path('user/', ShipmentOfUserAPIView.as_view())
]