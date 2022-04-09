from rest_framework.serializers import ModelSerializer
from account.models import Profile

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'twitter')

class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'profile')