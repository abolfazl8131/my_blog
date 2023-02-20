from django.shortcuts import render
from .serializers import UserRegisterSerializer , LoginSerializer , UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login, logout
# Create your views here.

class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]

class SessionAuthAPIView(CreateAPIView):
    #authentication_classes = (SessionAuthentication, MyBasicAuthentication)
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(UserSerializer(user).data)

class SessionLogoutAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated , )
    def post(self, request):
        logout(request)
        return Response()