from user.views.user_views import UserRegisterAPIView , UserUpdateAPIView 
from user.views.auth_views import SessionAuthAPIView , SessionLogoutAPIView
from user.views.profile_views import ProfileAPIView,ProfileUpdateAPIView,ProfileImageViewSet
from django.urls import path , include
from rest_framework.routers import DefaultRouter
# Create a router and register our viewsets with it.


urlpatterns = [
    
    path('register/', UserRegisterAPIView.as_view()),
    path('auth/' , SessionAuthAPIView.as_view()),
    path('logout/' , SessionLogoutAPIView.as_view()),
    path('update/' , UserUpdateAPIView.as_view()),
    path('myprofile' , ProfileAPIView.as_view()),
    path('profile/update/' , ProfileUpdateAPIView.as_view()),
    path('profile/image/' , ProfileImageViewSet.as_view())
    
] 
