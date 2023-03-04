from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from django.http import JsonResponse, HttpResponse
from .serializers import TodoSerializer
from .models import Todo
from user_profile.models import UserProfile

# Create your views here.

def say_hello(request):
    return HttpResponse('Hello World!')

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    #override perform_create to add user to todo
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    #override get_queryset to only return todos for the current user
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        #attempt to update points without changing how the serializer works
        data = self.request.data # type: ignore
        completed = data['completed']
        if self.request.completed == 'true' or self.request.completed == True: # type: ignore
            #add points to userprofile
            UserProfile.objects.filter(user=self.request.user).update(score=user.score + data['points']) # type: ignore
        serializer.save()  #user=self.request.user) trying without this first as that is default as far as I can find