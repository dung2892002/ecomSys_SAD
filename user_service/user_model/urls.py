from .views import UserRegistration
from django.urls import path

urlpatterns = [
    path('registration/', UserRegistration.as_view()),
]
