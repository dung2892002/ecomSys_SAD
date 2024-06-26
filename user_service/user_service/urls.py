"""user_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user_info import urls as info_urls
from user_login import urls as login_urls
from user_model import urls as registration_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include(info_urls)),
    path('api/v1/user/', include(login_urls)),
    path('api/v1/user/', include(registration_urls))
]
