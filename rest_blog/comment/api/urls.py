from django.urls import path

from comment.api.views import  CommentCreateAPIView, CommentListAPIView, CommentUpdateAPIView

app_name= "comment"
urlpatterns = [
  path('create/', CommentCreateAPIView.as_view(), name='create'),
  path('list/', CommentListAPIView.as_view(), name='list'),
  # update işleminde iki işlem birleştirildiği için artık delete ihtiyacı kalmadı, yukkarıdan impartu da silindi
  # path('delete/<pk>', CommentDeleteAPIView.as_view(), name='delete'),
  path('update/<pk>', CommentUpdateAPIView.as_view(), name='update'),
]