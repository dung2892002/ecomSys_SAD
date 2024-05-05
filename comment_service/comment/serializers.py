from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        
class CommentShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'rating', 'date_added', 'user_id']