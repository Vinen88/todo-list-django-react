from django.contrib import admin
from django.urls import path, include
from todo import views

urlpatterns = [
    path('', views.HomeView.as_view()),
]