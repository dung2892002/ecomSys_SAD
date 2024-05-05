from .views import AddCommentView, ListCommentOfProduct
from django.urls import path

urlpatterns = [
    path('add/', AddCommentView.as_view()),
    path('product/', ListCommentOfProduct.as_view()),
]
