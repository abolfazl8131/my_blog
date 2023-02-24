from django.shortcuts import render
from rest_framework import viewsets
from .models import Post , Comment , Category
from .serializers import PostListSerializer , PostDetailSerializer , CommentSerializer , CommentDetailSerializer,  PostCreateSerializer,CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import permissions
from permissons.permissons import IsAuthenticatedAndOwner
from rest_framework import generics
from django.db.models.query import QuerySet

class GetCategoryAPIView(generics.ListAPIView):

    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny , ]
    queryset = Category.objects.all()

class PostCreateAPIView(generics.CreateAPIView):

    serializer_class = PostCreateSerializer
    permission_classes = (permissions.IsAuthenticated , )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        serializer.author = request.user
        return super().create(request, *args, **kwargs)


class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = (permissions.IsAuthenticated , )

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        serializer.author = request.user
        return super().create(request, *args, **kwargs)

class PostListViewSet(viewsets.ReadOnlyModelViewSet):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [ filters.SearchFilter]
    search_fields = ['title' , 'body','categories__title']

    def get_queryset(self):
    
       
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.filter(show=True)
        return queryset


class PostDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    queryset = Post.objects.filter(show=True)


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
            if previous_comments.count() >= 1 and \
                previous_comments.post.show == False:
                return Response('sorry you cant comment this post any more!')
        return super().create(request, *args, **kwargs)


      
class CommentDetailViewSet(viewsets.ReadOnlyModelViewSet):
   
    serializer_class = CommentDetailSerializer
    permission_classes = (permissions.AllowAny , )
    http_method_names = ['get']
    #lookup_field = 'post__slug'
   
    def get_queryset(self , **kwargs):
        slug = self.request.GET.get('slug')
        if Post.objects.get(slug=slug).show == True:
           
            qs = Comment.objects.filter(post__slug=slug)
            return qs


class CommentDeleteAPIView(generics.DestroyAPIView):
   
    permission_classes = (IsAuthenticatedAndOwner , )
    lookup_field = 'pk'
    queryset = Comment.objects.all()
