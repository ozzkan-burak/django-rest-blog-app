from .serializers import RegisterSerializer
from .permissions import NotAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView,get_object_or_404, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from rest_framework.views import APIView 
from django.shortcuts import render
from rest_framework.response import Response

from account.api.serializers import UserSerializer, ChangePasswordSerializer

class ProfileView(RetrieveUpdateAPIView):
    """
    Profile view
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self, request, *args, **kwargs):
      queryset = self.get_queryset()
      obj = get_object_or_404(queryset, id = self.request.user.id)
      return obj

    def perfom_update(self, serializer):
      serializer.save(user = self.request.user)

class UpdatePassword(APIView):
    """
    Update password
    """

    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset):
      return self.request.user
    
    def put(self, request, * args, **kwargs):
      self.object = self.get_object()
      data = {
        'old_password': request.data['old_password'],
        'new_password': request.data['new_password']
      }
      serializer = ChangePasswordSerializer(data = request.data)
      if serializer.is_valid():
        # Check old password
        old_password = serializer.data.get("old_password")
        if not self.object.check_password(old_password):
          return Response({"old_password": ["Wrong password."]}, status = 400)
        # set_password also hashes the password that the user will get
        self.object.set_password(serializer.data.get("new_password"))
        self.object.save()
        update_session_auth_hash(request, self.object)
        return Response(status = 200)
      return Response(serializer.errors, status = 400)
    
class CreateUserView(CreateAPIView):
    """
    Create user
    """

    model = User.objects.all()
    permission_classes = [NotAuthenticated]
    serializer_class = RegisterSerializer