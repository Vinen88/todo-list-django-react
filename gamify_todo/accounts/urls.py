from django.urls import re_path, path
from .views import SignupView, GetCSRFToken, LoginView, LogoutView, CheckAuthenticatedView, DeleteAccountView, GetUsersView

urlpatterns = [
    path('register/', SignupView.as_view()),
    path('csrf_cookie/', GetCSRFToken.as_view()),    
    path('authenticated/', CheckAuthenticatedView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('delete_account/', DeleteAccountView.as_view()),
    path('get_users/', GetUsersView.as_view()),
]