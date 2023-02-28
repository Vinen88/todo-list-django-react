from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserProfileSerializer

class GetUserProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            username = user.username # type: ignore
            user = User.objects.get(id=user.id) # type: ignore
            user_profile = UserProfile.objects.get(user=user) # type: ignore
            user_profile = UserProfileSerializer(user_profile) # type: ignore
            return Response({ 'profile': user_profile.data, 'username': str(username)})
        except:
            return Response({ 'error': 'User not found' })
            
class UpdateUserProfileView(APIView):
    def put(self, request, format=None):
        try:
            user = self.request.user
            username = user.username # type: ignore
            data = self.request.data # type: ignore
            first_name = data['first_name']
            email = data['email']
            user = User.Object.get(id=user.id) # type: ignore
            UserProfile.objects.filter(user=user).update(first_name=first_name, email=email) # type: ignore
            user_profile = UserProfile.objects.get(user=user) # type: ignore
            return Response({ 'profile': user_profile.data, 'username': str(username)}) # type: ignore
        except:
            return Response({ 'error': 'profile update failed' })