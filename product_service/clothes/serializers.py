from rest_framework import serializers
from .models import Clothes, Producer, Style

class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = "__all__"

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"

class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = "__all__"

class ClothesInfoSerializers(serializers.ModelSerializer):
    producer = ProducerSerializer()
    style = StyleSerializer()
    
    class Meta:
        model = Clothes
        fields = "__all__"