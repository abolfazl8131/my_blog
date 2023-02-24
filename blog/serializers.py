from rest_framework import serializers
from .models import Post , Category, Comment
from user.serializers import AuthorSerializer , UserSerializer
from user.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title',)


class PostListSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    author = AuthorSerializer()
    id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Post
        fields = ('id' ,'slug' ,'title' , 'author' , 'img' , 'categories','date_published')


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = ('slug' ,'title' , 'author' , 'img' , 'categories',)
           
        
class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    author = AuthorSerializer()
    id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Post
        fields = ('id','title' , 'body' , 'date_published', 'last_update' , 'categories' , 'img','author' , 'slug')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('body' ,'post' , 'rating')


class CommentDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
   
    class Meta:
        model = Comment
        fields = ('id','user' , 'body' , 'rating' , 'date_published')
        