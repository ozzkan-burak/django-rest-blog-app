from rest_framework.generics import RetrieveUpdateAPIView,get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import render

from account.api.serializers import UserSerializer

class ProfileView(RetrieveUpdateAPIView):
    """
    Profile view
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
      queryset = self.get_queryset()
      obj = get_object_or_404(queryset, id = self.request.user.id)
      return obj

    def perfom_update(self, serializer):
      serializer.save(user = self.request.user)

    
