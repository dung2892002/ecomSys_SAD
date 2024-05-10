from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        
class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','product_type', 'product_id', 'quantity', 'date_added', 'pay_status']
        
class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user_id', 'quantity', 'date_added', 'pay_status']
