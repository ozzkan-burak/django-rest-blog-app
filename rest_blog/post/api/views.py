
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.mixins import CreateModelMixin
from post.models import Post
from post.api.permissions import IsOwner
from post.api.pagination import PostPagination
from post.api.serializers import PostSerializer, PostUpdateCreateSerializer

class PostListAPIView(ListAPIView, CreateModelMixin):
  serializer_class = PostSerializer
  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ['title', 'content']
  pagination_class = PostPagination 
  
  def get_queryset(self):
    queryset = Post.objects.filter(draft=False)
    return queryset
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
  
  def perform_create(self, serializer):
    serializer.save(user = self.request.user)
  
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
