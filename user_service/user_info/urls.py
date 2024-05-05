from .views import user_info
from django.urls import path

urlpatterns = [
    path('info/', user_info),
]
