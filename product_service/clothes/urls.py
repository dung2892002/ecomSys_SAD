from .views import ClothesAPIView, ProducerAPIView, StyleApiView, ClothesUpdateAPIView, ClothesSearchAPIView, ClothesDetailAPIView, ClothesDeleteAPIView, ClothesUpdateQuantity
from django.urls import path

urlpatterns = [
    path('producers/', ProducerAPIView.as_view()),
    path('styles/', StyleApiView.as_view()),
    path('clothes/', ClothesAPIView.as_view()),
    path('clothes/detail/', ClothesDetailAPIView.as_view()),
    path('clothes/search/', ClothesSearchAPIView.as_view()),
    path('clothes/edit/', ClothesUpdateAPIView.as_view()),
    path('clothes/delete/', ClothesDeleteAPIView.as_view()),
    path('clothes/quantity/', ClothesUpdateQuantity.as_view())
]
