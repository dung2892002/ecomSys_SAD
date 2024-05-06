from .views import AddOrderView, ListOrderOfUser, ListOrderProduct
from django.urls import path

urlpatterns = [
    path('add/', AddOrderView.as_view()),
    path('product/', ListOrderProduct.as_view()),
    path('user/', ListOrderOfUser.as_view()),
]
