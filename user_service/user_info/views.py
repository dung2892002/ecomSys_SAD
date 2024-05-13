from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from user_model.models import User, Address, Fullname
from user_model.serializers import UserInfoSerializer, AddressSerializer, FullnameSerializer, UserSerializer

class UserInfo(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserInfoSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserUpdateInfo(APIView):
    def put(self, request):
        user_id = request.query_params.get('user_id', None)
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        address = Address.objects.get(id=user.address.id)
        address_serializer = AddressSerializer(address, data=request.data.get('address'))
        fullname = Fullname.objects.get(id=user.fullname.id)
        fullname_serializer = FullnameSerializer(fullname, data=request.data.get('fullname'))
        errors = {}
        user_data = {
            'fullname': fullname.id,
            'address': address.id,
            'account': user.account.id,
            'email': request.data.get('email'),
            'mobile_number': request.data.get('mobile_number'),
        }
        user_serializer = UserSerializer(user,data=user_data)
        if not all([fullname_serializer.is_valid(), address_serializer.is_valid(), user_serializer.is_valid()]):
            errors.update({
                'fullname_errors': fullname_serializer.errors,
                'address_errors': address_serializer.errors,
                'user_errors': user_serializer.errors
            })
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        address_serializer.save()
        fullname_serializer.save()
        user_serializer.save()
        return Response({'message': 'User update success'}, status=status.HTTP_200_OK)