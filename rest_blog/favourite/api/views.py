from unicodedata import lookup
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView
from favourite.api.serializers import FavouriteListCreateAPISerializer ,FavouriteAPISerializer
from favourite.api.pagination import FavouritePagination
from favourite.api.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated

from favourite.models import Favourite

class FavouritelistCreateAPIView(ListCreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteListCreateAPISerializer
    paginatin_class = FavouritePagination
    permission_clases = (IsAuthenticated,IsOwner)
    
    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class FavouriteAPIView(RetrieveDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]
