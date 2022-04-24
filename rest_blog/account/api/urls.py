from django.urls import path

from .views import  ProfileView, UpdatePassword

app_name= "account"
urlpatterns = [
  path('me/', ProfileView.as_view(), name='account'),
  path('change-password', UpdatePassword.as_view(), name='change-password'),
]