from .views import UserLogin
from django.urls import path

urlpatterns = [
    path('login/', UserLogin.as_view()),
]
