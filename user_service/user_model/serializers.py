from rest_framework import serializers
from .models import Fullname, Address, Account, User


class FullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fullname
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"
        
class UserInfoSerializer(serializers.ModelSerializer):
    fullname = FullnameSerializer()
    address = AddressSerializer()
    
    class Meta:
        model = User
        fields = "__all__"

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'account']