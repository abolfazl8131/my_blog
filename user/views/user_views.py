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


class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    model = get_user_model()
    
    authentication_classes = []

class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated , ]
    queryset = get_user_model().objects.all()

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)