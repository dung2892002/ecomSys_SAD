from .models import Shipment
from .serializers import ShipmentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
class ShipmentAPIView(APIView):
    def post(self,request):
        serializer = ShipmentSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ShipmentOfUserAPIView(APIView):
    def get(self,request):
        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            shipments = Shipment.objects.filter(user_id=user_id)
            serializer = ShipmentSerializer(shipments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide user_id"}, status=status.HTTP_400_BAD_REQUEST) 
