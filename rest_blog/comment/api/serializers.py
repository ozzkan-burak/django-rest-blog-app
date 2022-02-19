from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from comment.models import Comment

class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created',]
        
    def validate(self, attrs):
      if(attrs['parent']):
        if(attrs['parent'].post != attrs['post']):
          raise serializers.ValidationError("Parent comment does not belong to this post")
        
      return attrs
    
    
class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'
        
    def get_replies(self, obj):
      if obj.any_children:
        return CommentListSerializer(obj.children(), many=True).data