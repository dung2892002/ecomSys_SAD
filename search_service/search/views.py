import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SearchSerializer
from .models import Search
# Create your views here.
class SearchAPIView(APIView):
    def post(self, request):
        key = request.data.get('key', '')
        user_id = request.data.get('user_id', '')
        Search.objects.create(key=key, user_id=user_id)
        result = self.search_book(key) + self.search_mobile(key) + self.search_clothes(key)
        return Response(result, status=status.HTTP_200_OK)
        
    def search_book(self, key):
        book_service_url = f"http://localhost:8008/api/v1/book/books/search/?query={key}"

        book_response = requests.get(book_service_url)
        if book_response.status_code == 200:
            return book_response.json()
        return []
    
    def search_mobile(self, key):
        mobile_service_url = f"http://localhost:8008/api/v1/mobile/mobiles/search/?query={key}"

        mobile_response = requests.get(mobile_service_url)
        if mobile_response.status_code == 200:
            return mobile_response.json()
        return []
    
    def search_clothes(self, key):
        clothes_service_url = f"http://localhost:8008/api/v1/clothes/clothes/search/?query={key}"

        clothes_response = requests.get(clothes_service_url)
        if clothes_response.status_code == 200:
            return clothes_response.json()
        return []
    
class HistorySearchAPIView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            searches = Search.objects.filter(user_id = user_id).all()
            serializer = SearchSerializer(searches, many=[True])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a user_id"}, status=status.HTTP_400_BAD_REQUEST)