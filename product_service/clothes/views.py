from .models import Clothes, Producer, Style
from .serializers import ClothesSerializer, ProducerSerializer, StyleSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
class ClothesAPIView(APIView):
    
    def get(self, request):
        clothes=Clothes.objects.filter()
        serializer = ClothesSerializer(clothes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ClothesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClothesDetailAPIView(APIView):
    def get(self,request):
        clothes_id = request.query_params.get('clothes_id', None)
        if clothes_id is not None:
            try:
                clothes = Clothes.objects.get(id=clothes_id)
            except Clothes.DoesNotExist:
                    return Response({'error': 'Clothes not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ClothesSerializer(clothes)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a clothes_id"}, status=status.HTTP_400_BAD_REQUEST) 

class ClothesUpdateAPIView(APIView):
    def put(self, request):
        clothes_id = request.query_params.get('clothes_id', None)
        if clothes_id is not None:
            try:
                clothes = Clothes.objects.get(id=clothes_id)
            except Clothes.DoesNotExist:
                    return Response({'error': 'Clothes not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ClothesSerializer(clothes, data=request.data, context={'request': request})
            if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
        else:
            return Response({"error": "Please provide a clothes_id"}, status=status.HTTP_400_BAD_REQUEST) 

class ClothesUpdateQuantity(APIView):
    def put(self,request):
        product_id = request.data.get('product_id')    
        quantity = request.data.get('quantity')
        try:
            clothes = Clothes.objects.get(id=product_id)
        except Clothes.DoesNotExist:
                return Response({'error': 'Clothes not found'}, status=status.HTTP_404_NOT_FOUND)
        quantity = int(quantity)
        if quantity < 0:
            return Response({'error': 'Quantity must be a positive integer'}, status=status.HTTP_400_BAD_REQUEST)
        if clothes.quantity < quantity:
            return Response({'error': 'Not enough product'}, status=status.HTTP_400_BAD_REQUEST)
        price = float(clothes.price.to_decimal())
        clothes.quantity -= quantity
        clothes.price = price
        clothes.save()
        return Response({'message': 'Quantity updated successfully'}, status=status.HTTP_200_OK)
    
class ClothesDeleteAPIView(APIView):
    def delete(self, request):
        clothes_id = request.query_params.get('clothes_id', None)
        if clothes_id is not None:
            try:
                clothes = Clothes.objects.get(id=clothes_id)
            except Clothes.DoesNotExist:
                    return Response({'error': 'Clothes not found'}, status=status.HTTP_404_NOT_FOUND)
            clothes.delete()
            return Response({"message": "Clothes delete succeed"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a clothes_id"}, status=status.HTTP_400_BAD_REQUEST) 

class ClothesSearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('query', None)
        if query is not None:
            clothes = Clothes.objects.filter(name__icontains=query)
            serializer = ClothesSerializer(clothes, many=True)
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
        
        
class StyleApiView(APIView):
    
    def get(self, request):
        styles=Style.objects.filter()
        serializer = StyleSerializer(styles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StyleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)