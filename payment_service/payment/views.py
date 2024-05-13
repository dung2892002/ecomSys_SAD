from .models import Payment
from .serializers import PaymentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
import json

class PaymentAPIView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if(serializer.is_valid()):
            order_response = self.order_update(request.data['order_id'])
            if order_response.status_code == 404:
                return Response({"error": json.loads(order_response.text)['error']}, status=status.HTTP_400_BAD_REQUEST)
            payment = serializer.save()
            shipment_response = self.ship_update(payment)
            return Response({"payment": "payment successfully", "shipment": "create shipment successfully", 
                             "order":json.loads(order_response.text)['message']}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def ship_update(self,payment):
        shipment = {
            'user_id' : payment.user_id,
            'order_id': payment.order_id,
            'payment_id': payment.id,
        }
        
        url = 'http://127.0.0.1:8006/api/v1/shipment/add/'
        response = requests.post(url, data=shipment)
        return response
    
    def order_update(self,order_id):
        url = f"http://localhost:8003/api/v1/order/update/?order_id={order_id}"
        response = requests.put(url)
        return response

class PaymentOfUser(APIView):
    def get(self,request):
        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            payments = Payment.objects.filter(user_id=user_id)
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide user_id"}, status=status.HTTP_400_BAD_REQUEST) 
