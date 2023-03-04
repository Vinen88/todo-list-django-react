from django.urls import path
from .views import GetUserProfileView, UpdateUserProfileView, GetLeaderboardView

urlpatterns = [
    path('user/', GetUserProfileView.as_view()),
    path('update/', UpdateUserProfileView.as_view()),
    path('leaderboard/', GetLeaderboardView.as_view()),
]