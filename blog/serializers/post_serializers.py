
from rest_framework import serializers
from blog.models import Post , Category, Comment
from user.serializers import AuthorSerializer , UserSerializer
from user.models import User



class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Category
        fields = ('id','title',)


class PostListSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    author = AuthorSerializer()
    id = serializers.IntegerField()
    class Meta:
        model = Post
        fields = ('id' ,'slug' ,'title' , 'author' , 'img' , 'categories','date_published')


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = ('slug' ,'title' , 'body', 'author' , 'img','categories')
           


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

