from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account
from django.contrib.auth.hashers import make_password
from .serializers import FullnameSerializer, AddressSerializer, AccountSerializer, UserSerializer

class UserRegistration(APIView):
    def post(self, request):
        data = request.data.copy()
        account_exists = Account.objects.filter(username=data.get('account')['username']).exists()
        if account_exists:
            return Response({'error': 'Username has been register'}, status=status.HTTP_400_BAD_REQUEST)
        if data.get('account')['password'] != data.get('confirm_password'):
            return Response({'error': 'Password and confirm password do not match'}, status=status.HTTP_400_BAD_REQUEST)
        
        data.pop('confirm_password')
        data['account']['password'] = make_password(data.get('account')['password'])
        fullname = {
            'first_name': 'No',
            'last_name': 'No'
        }
        address = {
            'no_house': 'No',
            'street': 'No',
            'ward': 'No',
            'district': 'No',
            'province': 'No'
        }
        fullname_serializer = FullnameSerializer(data=fullname)
        address_serializer = AddressSerializer(data=address)
        account_serializer = AccountSerializer(data=data.get('account'))
          
        errors = {}
        if not all([fullname_serializer.is_valid(), address_serializer.is_valid(), account_serializer.is_valid()]):
            errors.update({
                'fullname_errors': fullname_serializer.errors,
                'address_errors': address_serializer.errors,
                'account_errors': account_serializer.errors,
            })
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        fullname_instance = fullname_serializer.save()
        address_instance = address_serializer.save()
        account_instance = account_serializer.save()

        user_data = {
            'fullname': fullname_instance.id,
            'address': address_instance.id,
            'account': account_instance.id,
            'email': 'No',
            'mobile_number': 'No'
        }
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
