from .views import AddOrderView, ListOrderOfUser, UpdateStatus
from django.urls import path

urlpatterns = [
    path('add/', AddOrderView.as_view()),
    path('user/', ListOrderOfUser.as_view()),
    path('update/', UpdateStatus.as_view())
]
