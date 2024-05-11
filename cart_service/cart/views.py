import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem
from .serializers import CartItemSerializer, UpdateCartItemSerializer

class AddToCartView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        product_id = request.data.get('product_id')
        product_type = request.data.get('product_type')
        cart_item = CartItem.objects.filter(user_id=user_id, product_id=product_id, product_type=product_type).first()
        if cart_item:
            serializer = UpdateCartItemSerializer(instance=cart_item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = CartItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CartView(APIView):    
    def get(self,request):
        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            cart_items = CartItem.objects.filter(user_id = user_id)
            total_price_cart = 0
            data = []
            for cart_item in cart_items:
                product = self.get_product(cart_item.product_type, cart_item.product_id)
                total_price_cart += cart_item.quantity * float(product.get('price', 0))
                item = {
                        'id': cart_item.id,
                        'product': product,
                        'quantity': cart_item.quantity,
                        'total_price': cart_item.quantity * float(product.get('price', 0))
                    }
                data.append (item)
            response = {
                'cart':data,
                'total_price_cart': total_price_cart
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a user_id"}, status=status.HTTP_400_BAD_REQUEST) 

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

class DeleteCartItemView(APIView):
    def delete(self, request):
        cart_item_id = request.query_params.get('cart_item_id', None)
        if cart_item_id is not None:
            try:
                cart_item = CartItem.objects.get(id = cart_item_id)
            except CartItem.DoesNotExist:
                return Response({'error': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)
            cart_item.delete()
            return Response({"message": "Cart item delete succeed"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a cart_item_id"}, status=status.HTTP_400_BAD_REQUEST) 
            
                