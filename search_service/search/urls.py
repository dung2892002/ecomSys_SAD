from .views import SearchAPIView, HistorySearchAPIView
from django.urls import path

urlpatterns = [
    path('', SearchAPIView.as_view()),
    path('user/', HistorySearchAPIView.as_view()),
    # path('delete/', DeleteCartItemView.as_view()),
]
