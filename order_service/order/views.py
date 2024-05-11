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
class UpdateStatus(APIView):
    def put(self, request):
        order_id = request.query_params.get('order_id', None)
        if order_id is not None:
            try:
                order = Order.objects.get(id=order_id)
            except Order.DoesNotExist:
                    return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
            if order.pay_status == True:
                return Response({'error': 'The order has been paid'}, status=status.HTTP_404_NOT_FOUND)
            order.pay_status = True
            order.save()
            return Response({'message': 'Payment status updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a order_id"}, status=status.HTTP_400_BAD_REQUEST) 
class ListOrderOfUser(APIView):
    def get(self, request):
        user_id = request.data.get('user_id')
        orders = Order.objects.filter(user_id=user_id)
        data = []
        for order in orders:
            product = get_product(order.product_type, order.product_id)
            item = {
                    'id': order.id,
                    'product': product,
                    'quantity': order.quantity,
                    'total_price': order.quantity * float(product.get('price', 0)),
                    'date_added': order.date_added,
                    'pay_status': order.pay_status
                }
            data.append (item)
        return Response(data, status=status.HTTP_200_OK)

class ListOrderProduct(APIView):
    def get(self, request):
        product_type = request.data.get('product_type')
        product_id = request.data.get('product_id')
        orders = Order.objects.filter(product_type=product_type, product_id=product_id)
        serializer = OrderProductSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def get_product(product_type, product_id):
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