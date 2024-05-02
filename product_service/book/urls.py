from .views import BookAPIView, AuthorAPIView, PublisherApiView, CategoryAPIView, BookSearchAPIView, BookDetailAPIView, BookUpdateAPIView
from django.urls import path

urlpatterns = [
    path('authors/', AuthorAPIView.as_view()),
    path('categories/', CategoryAPIView.as_view()),
    path('publishers/', PublisherApiView.as_view()),
    path('books/', BookAPIView.as_view()),
    path('books/detail/', BookDetailAPIView.as_view()),
    path('books/search/', BookSearchAPIView.as_view()),
    path('books/edit/', BookUpdateAPIView.as_view())
]
