from .views import user_login
from django.urls import path

urlpatterns = [
    path('login/', user_login),
]
