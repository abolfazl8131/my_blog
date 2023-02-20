from rest_framework import serializers
from .models import Author , User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'last_name','email')
        
class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Author
        fields = ('user' , )

from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True,style={'input_type': 'password', 'placeholder': 'Password'})

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "username", "password", )

from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,style={'input_type': 'password', 'placeholder': 'Password'})

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect username or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}