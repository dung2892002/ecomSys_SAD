import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer,OrderUserSerializer,OrderProductSerializer

class AddOrderView(APIView):
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            product = self.get_product(request.data.get("product_type"), request.data.get("product_id"))
            if (request.data.get("quantity") > product.get('quantity')):
                return Response({"error": "Not enough products"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get_product(self, product_type, product_id):
        if product_type == 'book':
            product_url = f"http://localhost:8008/api/v1/book/books/detail/?book_id={product_id}"
        if product_type == 'mobile':
            product_url = f"http://localhost:8008/api/v1/mobile/mobiles/detail/?mobile_id={product_id}"
        if product_type == 'clothes':
            product_url = f"http://localhost:8008/api/v1/clothes/clothes/detail/?clothes_id={product_id}"
        response = requests.get(product_url)
        if response.status_code == 200:
            return response.json()
        return None
    

class ListOrderOfUser(APIView):
    def get(self, request):
        user_id = request.data.get('user_id')
        orders = Order.objects.filter(user_id=user_id)
        serializer = OrderUserSerializer(orders, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ListOrderProduct(APIView):
    def get(self, request):
        product_type = request.data.get('product_type')
        product_id = request.data.get('product_id')
        orders = Order.objects.filter(product_type=product_type, product_id=product_id)
        serializer = OrderProductSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)