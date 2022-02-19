from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='post:detail', lookup_field='slug')
    
    username = serializers.SerializerMethodField(method_name='username_new')
    class Meta:
        model = Post
        fields = ['username','title', 'content', 'image', 'url', 'created', 'modified_by']
        
    def username_new(self,obj):
        return str(obj.user.username)
        
class PostUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = ['title', 'content','image', 'slug', 'created']
        
    def save(self, **kwargs):
        return True