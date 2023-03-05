from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import UserProfile
from .serializers import UserProfileSerializer



class GetUserProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            username = user.username # type: ignore
            user_profile = UserProfile.objects.get(user=user) 
            user_profile = UserProfileSerializer(user_profile) 
            return Response({ 'profile': user_profile.data, 'username': str(username)})
        except:
            return Response({ 'error': 'User not found' })
            
class UpdateUserProfileView(APIView):
    def put(self, request, format=None):
        user = self.request.user
        username = user.username # type: ignore
        data = self.request.data # type: ignore
        first_name = data['first_name']
        email = data['email']
        UserProfile.objects.filter(user=user).update(first_name=first_name, email=email)
        user_profile = UserProfile.objects.get(user=user) 
        user_profile = UserProfileSerializer(user_profile)
        return Response({ 'profile': user_profile.data, 'username': str(username)}) 
    #except:
        #    return Response({ 'error': 'profile update failed' })
        
class GetLeaderboardView(APIView):
    def get(self, request, format=None):
        #might want to try just making it return the username and the score only
        top_profiles = UserProfile.objects.all().order_by('-points')[:10]
        serialized_profiles = []
        for user in top_profiles:
            user_data = User.objects.get(id=user.id) #type: ignore
            serialized_profiles.append({"user":user_data.username, "points": user.points}) #type: ignore
        return Response({ 'top_users': serialized_profiles})
        