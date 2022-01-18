from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user','title', 'content', 'image', 'slug', 'created', 'modified_by']
        
class PostUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = ['title', 'content','image', 'slug', 'created']
        
    def save(self, **kwargs):
        return True