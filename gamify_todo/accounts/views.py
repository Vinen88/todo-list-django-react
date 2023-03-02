from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from user_profile.models import UserProfile
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from .serializers import UserSerializer

@method_decorator(csrf_protect, name='dispatch')
class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        try:
            if User.is_authenticated:
                return Response({'isAuthenticated': True})
            return Response({'isAuthenticated': False})
        except:
            return Response({'error': 'Something went wrong when checking if user is authenticated'})

@method_decorator(csrf_protect, name='dispatch')        
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request, format=None):
        data = self.request.data # type: ignore
        username = data['username']
        password = data['password']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return Response({'success': 'User logged in successfully', 'username': username})
            return Response({'error': 'Invalid credentials Auth failed'})
        except:
            return Response({'error': 'Something went wrong when logging in'})

class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({'success': 'User logged out successfully'})
        except:
            return Response({'error': 'Something went wrong when logging out'})

@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request, format=None):
        data = self.request.data # type: ignore
        username = data['username']
        password = data['password']
        re_password = data['re_password']
        if password == re_password:
            try:
                if User.objects.filter(username=username).exists():
                    return Response({'error': 'Username is already taken'})
                else:
                    if len(password) < 6:
                        return Response({'error': 'Password must be at least 6 characters'})
                    else:
                        print("creating user")
                        user = User.objects.create_user(username=username, password=password)
                        user.save()
                        user = User.objects.get(id=user.id) #type: ignore
                        user_profile = UserProfile(user=user, points=0) 
                        user_profile.save()
                        return Response({'success': 'User created successfully'})
            except:
                return Response({'error': 'Something went wrong when creating user'})
        else:
            return Response({'error': 'Passwords do not match'})

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, format=None):
        return Response({'success': 'CSRF cookie set'})
    

class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        try:
            user = self.request.user
            user = User.objects.filter(id=user.id).delete() #type: ignore
        except:
            return Response({'error': 'Something went wrong when deleting account'})
        return Response({'success': 'Account deleted successfully'})

class GetUsersView(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, format=None):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except:
            return Response({'error': 'Something went wrong when getting users'})