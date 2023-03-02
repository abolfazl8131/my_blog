from django.shortcuts import render
from user.serializers import UserRegisterSerializer , LoginSerializer , UserSerializer , UserUpdateSerializer,AuthorSerializer,AuthorUpdateSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView , UpdateAPIView , RetrieveUpdateAPIView , RetrieveAPIView
from rest_framework.response import Response 
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from permissons.permissons import IsAuthenticatedAndOwner
from rest_framework import status
from user.models import Author
from rest_framework import viewsets
from user.serializers import AuthorImageSerializer
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect , csrf_exempt

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