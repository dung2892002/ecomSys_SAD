from .views import AddOrderView, ListOrderOfUser, ListOrderProduct, UpdateStatus
from django.urls import path

urlpatterns = [
    path('add/', AddOrderView.as_view()),
    path('product/', ListOrderProduct.as_view()),
    path('user/', ListOrderOfUser.as_view()),
    path('update/', UpdateStatus.as_view())
]
