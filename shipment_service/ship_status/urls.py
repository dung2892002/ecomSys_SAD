from .views import shipment_reg_update, shipment_status
from django.urls import path

urlpatterns = [
    path('update/', shipment_reg_update),
    path('status/', shipment_status),
]
