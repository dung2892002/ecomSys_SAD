from .views import registration_req
from django.urls import path

urlpatterns = [
    path('registration/', registration_req),
]
