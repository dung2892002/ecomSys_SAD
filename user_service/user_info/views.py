from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from user_model.models import User
from user_model.serializers import UserInfoSerializer

class UserInfo(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserInfoSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)