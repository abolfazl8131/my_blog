from django.shortcuts import render
from rest_framework import viewsets
from .models import Post , Comment
from .serializers import PostListSerializer , PostDetailSerializer , CommentSerializer , CommentDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import permissions

class PostListViewSet(viewsets.ReadOnlyModelViewSet):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [ filters.SearchFilter]
    search_fields = ['title' , 'body','categories__title']



class PostDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    queryset = Post.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
   
    serializer_class = CommentSerializer
    queryset = Comment.objects.none()
    permission_classes = (permissions.IsAuthenticated , )
    http_method_names = ['post']

    def perform_create(self, serializer):

        
        if self.request.user.is_authenticated:

            instance = serializer.save(user=self.request.user)
        else:
            instance = serializer.save() 
    
    def create(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:

            if Comment.objects.filter(user=request.user , post=request.data.get('post')).count() >= 1:
                return Response('sorry you cant comment this post any more!')
        return super().create(request, *args, **kwargs)


      
class CommentDetailViewSet(viewsets.ReadOnlyModelViewSet):
   
    serializer_class = CommentDetailSerializer
    permission_classes = (permissions.AllowAny , )
    http_method_names = ['get']
    #lookup_field = 'post__slug'
   

    def get_queryset(self , **kwargs):
        slug = self.request.GET.get('slug')
        qs = Comment.objects.filter(post__slug=slug)
        return qs

from .permissons import IsAuthenticatedAndOwner
from rest_framework import generics

class CommentDeleteAPIView(generics.DestroyAPIView):
   
    permission_classes = (IsAuthenticatedAndOwner , )
    lookup_field = 'pk'
    queryset = Comment.objects.all()
