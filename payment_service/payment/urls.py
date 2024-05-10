from .views import PaymentAPIView, PaymentOfUser
from django.urls import path

urlpatterns = [
    path('add/', PaymentAPIView.as_view()),
    path('user/', PaymentOfUser.as_view())
]