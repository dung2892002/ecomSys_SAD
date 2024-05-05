import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer, CommentShowSerializer

class AddCommentView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListCommentOfProduct(APIView):
    def get(self, request):
        product_type = request.data.get('product_type')
        product_id = request.data.get('product_id')
        comments = Comment.objects.filter(product_type=product_type, product_id=product_id)
        serializer = CommentShowSerializer(comments, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)