
from django.shortcuts import render
from rest_framework import viewsets
from blog.models import Post , Comment , Category
from blog.serializers import (PostListSerializer , 
PostDetailSerializer , 
CommentSerializer ,
 CommentDetailSerializer,  
 PostCreateSerializer,CategorySerializer )
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import permissions
from permissons.permissons import IsAuthenticatedAndOwner
from rest_framework import generics
from django.db.models.query import QuerySet
from permissons.permissons import IsAuthenticatedAndOwner
from django.views.decorators.csrf import csrf_protect , csrf_exempt
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication
from blog.models import Author

class GetCategoryAPIView(generics.ListAPIView):

    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny , ]
    queryset = Category.objects.all()

class PostCreateAPIView(generics.CreateAPIView):

    serializer_class = PostCreateSerializer
    permission_classes = (permissions.IsAuthenticated , )
   
    def perform_create(self, serializer):
        author = Author.objects.get(user = self.request.user)
        serializer.save(author=author)
    

    

# class PostTagViewSet(viewsets.ModelViewSet):

#     serializer_class = PostCreateSerializer
#     permission_classes = [IsAuthenticatedAndOwner , ]

#     def get_object(self):
#         posts = Post.objects.all()
#         post = get_object_or_404(posts, pk=self.request.GET.get('post_id'))
#         return post

#     def partial_update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)

class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = (permissions.IsAuthenticated ,)
    lookup_field = 'id'
    queryset = Post.published.all()

    # def get_object(self):
    #     posts = Post.objects.all()
    #     post = get_object_or_404(posts, pk=self.request.GET.get('post_id'))
    #     return post

    def check_permissions(self, request):
        if self.get_object().author == request.user:
            return True
        return False
        
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class PostListViewSet(viewsets.ReadOnlyModelViewSet):
    model = Post
    queryset = Post.published.all()
    serializer_class = PostListSerializer
    filter_backends = [ filters.SearchFilter]
    search_fields = ['title' , 'body','categories__title']
  

class FilterPostWithCategory(generics.ListAPIView):
   
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.published.filter(categories__title__contains= self.kwargs.get('category'))

from django.http import JsonResponse

class PostDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    
    def get(self , request):
        
        slug = self.request.GET.get('slug')
       
        try:
            article = Post.published.get(slug=slug)

            ip_addr = self.request.ip_address

            if ip_addr not in article.hits.all():
                
                article.hits.add(ip_addr)
        except:
            raise Exception('there is a problem when opening the article')
        
        serializer = PostDetailSerializer(article)
       
        return JsonResponse(serializer.data)


