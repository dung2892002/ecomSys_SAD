from .models import Mobile, Producer, Type
from .serializers import MobileSerializer, ProducerSerializer, TypeSerializer, MobileInfoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
class MobileAPIView(APIView):
    
    def get(self, request):
        mobiles=Mobile.objects.filter()
        serializer = MobileInfoSerializer(mobiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MobileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MobileDetailAPIView(APIView):
    def get(self,request):
        mobile_id = request.query_params.get('mobile_id', None)
        if mobile_id is not None:
            try:
                mobile = Mobile.objects.get(id=mobile_id)
            except Mobile.DoesNotExist:
                    return Response({'error': 'Mobile not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = MobileInfoSerializer(mobile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a mobile_id"}, status=status.HTTP_400_BAD_REQUEST) 

class MobileUpdateAPIView(APIView):
    def put(self, request):
        mobile_id = request.data.get('id', None)
        if mobile_id is not None:
            try:
                mobile = Mobile.objects.get(id=mobile_id)
            except Mobile.DoesNotExist:
                    return Response({'error': 'Mobile not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = MobileSerializer(mobile, data=request.data, context={'request': request})
            if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
        else:
            return Response({"error": "Please provide a mobile_id"}, status=status.HTTP_400_BAD_REQUEST) 

class MobileUpdateQuantity(APIView):
    def put(self,request):
        product_id = request.data.get('product_id')    
        quantity = request.data.get('quantity')
        try:
            mobile = Mobile.objects.get(id=product_id)
        except Mobile.DoesNotExist:
                return Response({'error': 'Mobile not found'}, status=status.HTTP_404_NOT_FOUND)
        quantity = int(quantity)
        if quantity < 0:
            return Response({'error': 'Quantity must be a positive integer'}, status=status.HTTP_400_BAD_REQUEST)
        if mobile.quantity < quantity:
            return Response({'error': 'Not enough product'}, status=status.HTTP_400_BAD_REQUEST)
        price = float(mobile.price.to_decimal())
        mobile.quantity -= quantity
        mobile.sold += quantity
        mobile.price = price
        mobile.save()
        return Response({'message': 'Quantity updated successfully'}, status=status.HTTP_200_OK)
    
class MobileDeleteAPIView(APIView):
    def delete(self, request):
        mobile_id = request.data.get('id', None)
        if mobile_id is not None:
            try:
                mobile = Mobile.objects.get(id=mobile_id)
            except Mobile.DoesNotExist:
                    return Response({'error': 'Mobile not found'}, status=status.HTTP_404_NOT_FOUND)
            mobile.delete()
            return Response({"message": "Mobile delete succeed"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a mobile_id"}, status=status.HTTP_400_BAD_REQUEST) 
        
class MobileSearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('query', None)
        if query is not None:
            mobiles = Mobile.objects.filter(name__icontains=query)
            serializer = MobileInfoSerializer(mobiles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a search query"}, status=status.HTTP_400_BAD_REQUEST) 

class ProducerAPIView(APIView):
    
    def get(self, request):
        producers=Producer.objects.filter()
        serializer = ProducerSerializer(producers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProducerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TypeApiView(APIView):
    
    def get(self, request):
        types=Type.objects.filter()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        