from .views import UserRegisterAPIView , SessionAuthAPIView , SessionLogoutAPIView
from django.urls import path , include
from rest_framework.routers import DefaultRouter
# Create a router and register our viewsets with it.


urlpatterns = [
    path('register/', UserRegisterAPIView.as_view()),
    path('auth/' , SessionAuthAPIView.as_view()),
    path('logout/' , SessionLogoutAPIView.as_view())
    
] 
