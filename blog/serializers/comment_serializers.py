
from rest_framework import serializers
from blog.models import Post , Category, Comment
from user.serializers import AuthorSerializer , UserSerializer
from user.models import User


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('body' ,'post' , 'rating')


class CommentDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
   
    class Meta:
        model = Comment
        fields = ('id','user' , 'body' , 'rating' , 'date_published')
        