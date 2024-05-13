from .views import UserInfo, UserUpdateInfo
from django.urls import path

urlpatterns = [
    path('info/', UserInfo.as_view()),
    path('info/update/', UserUpdateInfo.as_view()),
]
