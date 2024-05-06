from decimal import Decimal
from .models import Book, Author, Category, Publisher
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
class BookAPIView(APIView):
    
    def get(self, request):
        books=Book.objects.filter()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailAPIView(APIView):
    def get(self,request):
        book_id = request.query_params.get('book_id', None)
        if book_id is not None:
            try:
                book = Book.objects.get(id=book_id)
            except Book.DoesNotExist:
                    return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a book_id"}, status=status.HTTP_400_BAD_REQUEST) 

class BookUpdateAPIView(APIView):
    def put(self, request):
        book_id = request.query_params.get('book_id', None)
        if book_id is not None:
            try:
                book = Book.objects.get(id=book_id)
            except Book.DoesNotExist:
                    return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = BookSerializer(book, data=request.data, context={'request': request})
            if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
        else:
            return Response({"error": "Please provide a book_id"}, status=status.HTTP_400_BAD_REQUEST) 
        
class BookUpdateQuantity(APIView):
    def put(self,request):
        product_id = request.data.get('product_id')    
        quantity = request.data.get('quantity')
        try:
            book = Book.objects.get(id=product_id)
        except Book.DoesNotExist:
                return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        quantity = int(quantity)
        if quantity < 0:
            return Response({'error': 'Quantity must be a positive integer'}, status=status.HTTP_400_BAD_REQUEST)
        if book.quantity < quantity:
            return Response({'error': 'Not enough product'}, status=status.HTTP_400_BAD_REQUEST)
        price = float(book.price.to_decimal())
        book.quantity -= quantity
        book.price = price
        book.save()
        return Response({'message': 'Quantity updated successfully'}, status=status.HTTP_200_OK)

class BookDeleteAPIView(APIView):
    def delete(self, request):
        book_id = request.query_params.get('book_id', None)
        if book_id is not None:
            try:
                book = Book.objects.get(id=book_id)
            except Book.DoesNotExist:
                    return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
            book.delete()
            return Response({"message": "Book delete succeed"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a book_id"}, status=status.HTTP_400_BAD_REQUEST) 
        
class BookSearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('query', None)
        if query is not None:
            books = Book.objects.filter(title__icontains=query)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a search query"}, status=status.HTTP_400_BAD_REQUEST) 

class AuthorAPIView(APIView):
    
    def get(self, request):
        authors=Author.objects.filter()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PublisherApiView(APIView):
    
    def get(self, request):
        publisher=Publisher.objects.filter()
        serializer = PublisherSerializer(publisher, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CategoryAPIView(APIView):
    def get(self, request):
        category=Category.objects.filter()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        