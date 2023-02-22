from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.

class HomeView(APIView):
    def get(self, request):
        return JsonResponse({'message': 'Hello, World from django and docker!'})