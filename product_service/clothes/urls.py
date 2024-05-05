from .views import ClothesAPIView, ProducerAPIView, StyleApiView, ClothesUpdateAPIView, ClothesSearchAPIView, ClothesDetailAPIView
from django.urls import path

urlpatterns = [
    path('producers/', ProducerAPIView.as_view()),
    path('styles/', StyleApiView.as_view()),
    path('clothes/', ClothesAPIView.as_view()),
    path('clothes/detail/', ClothesDetailAPIView.as_view()),
    path('clothes/search/', ClothesSearchAPIView.as_view()),
    path('clothes/edit/', ClothesUpdateAPIView.as_view())
]
