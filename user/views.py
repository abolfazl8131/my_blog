from django.shortcuts import render
from .serializers import UserRegisterSerializer , LoginSerializer , UserSerializer , UserUpdateSerializer,AuthorSerializer,AuthorUpdateSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView , UpdateAPIView , RetrieveUpdateAPIView , RetrieveAPIView
from rest_framework.response import Response 
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from permissons.permissons import IsAuthenticatedAndOwner
from rest_framework import status
from .models import Author
from rest_framework import viewsets
from .serializers import AuthorImageSerializer
# Create your views here.
from django.http import JsonResponse

class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]

class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated , ]
    queryset = get_user_model().objects.all()

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileAPIView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated , ]
    serializer_class = AuthorSerializer
    
    def get(self , request):
        profile = Author.objects.get(user = request.user)
        serializer = self.serializer_class(profile)
       
        print(serializer.data)
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