from rest_framework import serializers
from .models import Author , User

class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'last_name','email')
        
class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    image = serializers.FileField()
    class Meta:
        model = Author
        fields = ('user' , 'description' , 'image')

class AuthorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('description' ,)

class AuthorImageSerializer(serializers.Serializer):
        image = serializers.ImageField()

from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True,style={'input_type': 'password', 'placeholder': 'Password'})

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email']
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "username", "password", 'first_name' , 'last_name' , 'email')

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name' , 'last_name']


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