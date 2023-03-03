from django.shortcuts import render
from rest_framework import viewsets
from blog.models import Post , Comment , Category
from blog.serializers import PostListSerializer , PostDetailSerializer , CommentSerializer , CommentDetailSerializer,  PostCreateSerializer,CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import permissions
from permissons.permissons import IsAuthenticatedAndOwner
from rest_framework import generics
from django.db.models.query import QuerySet
from permissons.permissons import IsAuthenticatedAndOwner



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
            previous_comments = Comment.objects.filter(user=request.user , post=request.data.get('post'))
            if previous_comments.count() >= 1:
                return Response('sorry you cant comment this post any more!')
        return super().create(request, *args, **kwargs)


      
class CommentDetailViewSet(viewsets.ReadOnlyModelViewSet):
   
    serializer_class = CommentDetailSerializer
    permission_classes = (permissions.AllowAny , )
    http_method_names = ['get']
    lookup_field = 'slug'
 
    def get_queryset(self , **kwargs):

        slug = self.request.GET.get('slug')
        
        if Post.published.filter(slug=slug).exists():
        
            qs = Comment.published.filter(post__slug=slug)
            
            return qs


class CommentDeleteAPIView(generics.DestroyAPIView):
   
    permission_classes = (IsAuthenticatedAndOwner , )
    lookup_field = 'pk'
    queryset = Comment.published.all()
