import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer,OrderUserSerializer,OrderProductSerializer
import json

class AddOrderView(APIView):
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            product_type = request.data.get("product_type")
            product_id = request.data.get("product_id")
            quantity = request.data.get("quantity")
            quantity = int(quantity)
            response = self.check_product_quantity_and_update(product_type, product_id, quantity)
            if response.status_code != 200:
                error_message = json.loads(response.text)['error']
                return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def check_product_quantity_and_update(self, product_type, product_id, quantity):
        if product_type == 'book':
            product_url = "http://localhost:8008/api/v1/book/books/quantity/"
        elif product_type == 'mobile':
            product_url = "http://localhost:8008/api/v1/mobile/mobiles/quantity/"
        elif product_type == 'clothes':
            product_url = "http://localhost:8008/api/v1/clothes/clothes/quantity/"
        else:
            return False
        
        payload = {
            'product_id': product_id,
            'quantity': int(quantity)
        }
        
        response = requests.put(product_url, data=payload)
        return response

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