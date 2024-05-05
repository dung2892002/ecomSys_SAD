from .views import get_payment, user_transaction_info
from django.urls import path

urlpatterns = [
    path('update/', get_payment),
    path('status/', user_transaction_info),
]
