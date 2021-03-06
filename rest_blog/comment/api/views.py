from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin

from comment.api.serializers import CommentCreateSerializer, CommentListSerializer, CommentDeleteUpdateSerializer
from comment.models import Comment

from comment.api.permissions import IsOwner
from comment.api.paginations import CommentPagination



class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    pagination_class = CommentPagination
    def get_queryset(self):
      queryset = Comment.objects.filter(parent = None)
      query = self.request.GET.get('q')
      
      if query:
        queryset = queryset.filter(post = query)
        
      return queryset
      
    
# bir sonraki classda iki işlemi birleştirdiğimiz için artık bu class a ihtiyaç kalmadı
    
# class CommentDeleteAPIView(DestroyAPIView , UpdateModelMixin, RetrieveModelMixin):
#   queryset = Comment.objects.all()
#   serializer_class = CommentDeleteUpdateSerializer
#   lookup_field = 'pk'
#   permissions_classes = [IsOwner]
  
#   def put(self, request, *args, **kwargs):
#     return self.update(request, *args, **kwargs)
  
#   def get(self, request, * args, **kwargs):
#     return self.retrieve(request, *args, **kwargs)

class CommentUpdateAPIView(DestroyModelMixin,UpdateAPIView, RetrieveAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentDeleteUpdateSerializer
  lookup_field = 'pk'
  permissions_classes = [IsOwner]
  
  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)