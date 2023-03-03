
from rest_framework import serializers
from blog.models import Post , Category, Comment
from user.serializers import AuthorSerializer , UserSerializer
from user.models import User



class CategorySerializer(serializers.ModelSerializer):
  
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
           


class PostDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    author = AuthorSerializer()
    id = serializers.IntegerField(write_only=True)
    title = serializers.CharField()
    hits_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        
        fields = ('id', 'title' , 'body' , 'date_published', 'last_update' , 'categories' , 'img','author' , 'slug','hits_count')

    def get_hits_count(self,  instance):
        return instance.hits.count()
        

