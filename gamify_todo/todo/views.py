from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from django.http import JsonResponse, HttpResponse
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

def say_hello(request):
    return HttpResponse('Hello World!')

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()