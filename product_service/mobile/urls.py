from .views import MobileAPIView, ProducerAPIView, TypeApiView, MobileUpdateAPIView, MobileSearchAPIView, MobileDetailAPIView
from django.urls import path

urlpatterns = [
    path('producers/', ProducerAPIView.as_view()),
    path('types/', TypeApiView.as_view()),
    path('mobiles/', MobileAPIView.as_view()),
    path('mobiles/detail/', MobileDetailAPIView.as_view()),
    path('mobiles/search/', MobileSearchAPIView.as_view()),
    path('mobiles/edit/', MobileUpdateAPIView.as_view())
]
