from django.urls import path
from favourite.api.views import FavouritelistCreateAPIView

app_name="favourite"
urlpatterns =[
  path('list-create', FavouritelistCreateAPIView.as_view(), name='list-create'),
]