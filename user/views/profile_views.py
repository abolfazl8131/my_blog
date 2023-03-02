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

class ProfileAPIView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated , ]
    serializer_class = AuthorSerializer
    
    
    def get(self , request):
        profile = Author.objects.get(user = request.user)
        serializer = self.serializer_class(profile)
       
        return JsonResponse(serializer.data)

class ProfileUpdateAPIView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated , ]
    serializer_class = AuthorUpdateSerializer
    
    def update(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(user=request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileImageViewSet(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated , ]
    serializer_class = AuthorImageSerializer

    def update(self, request, *args, **kwargs):
       file = request.FILES
       a = Author.objects.get(user=request.user.id)
       a.image = file
       a.save()
       return Response('ok' , status=200)
    