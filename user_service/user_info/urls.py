from .views import UserInfo
from django.urls import path

urlpatterns = [
    path('info/', UserInfo.as_view()),
]
