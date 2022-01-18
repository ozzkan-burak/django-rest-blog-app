from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from post.models import Post
from post.api.serializers import PostSerializer, PostUpdateCreateSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from post.api.permissions import IsOwner

class PostListAPIView(ListAPIView):
  serializer_class = PostSerializer
  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ['title']
  
  def get_queryset(self):
    queryset = Post.objects.filter(draft=False)
    return queryset
  
class PostDetailAPIView(RetrieveAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  lookup_field = 'slug'

class PostDeleteAPIView(DestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  lookup_field = 'slug'
  permission_classes = [IsOwner]

class PostUpdateAPIView(RetrieveUpdateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostUpdateCreateSerializer
  lookup_field = 'slug'
  permission_classes = [IsOwner]
  
  def perform_update(self, serializer):
    serializer.save(modified_by=self.request.user)

class PostCreateAPIView(CreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostUpdateCreateSerializer
  permission_classes = [IsAuthenticated]
  
  def perform_create(self, serializer):
    serializer.save(user=self.request.user)
