from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from user_model.models import Account, User
from django.contrib.auth.hashers import check_password
    
class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            account = Account.objects.get(username=username)
        except Account.DoesNotExist:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
        if not check_password(password, account.password):
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(account = account)
        return Response({'message': 'Login successful', 'user_id': user.id}, status=status.HTTP_200_OK)
