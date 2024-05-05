from .views import AddToCartView, CartView, DeleteCartItemView
from django.urls import path

urlpatterns = [
    path('add-to-cart/', AddToCartView.as_view()),
    path('user/', CartView.as_view()),
    path('delete/', DeleteCartItemView.as_view()),
]
