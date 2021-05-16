from rest_framework import serializers
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate, get_user_model
from rest_framework_jwt.settings import api_settings

from .models import User, Post, Profile

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post  # 사용할 모델
        fields = ['id', 'text', 'user', 'createdDate', 'updatedDate']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        post = Post.objects.create(user=user_data, **validated_data)
        post.user_id = user_data
        return post


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile  # 사용할 모델
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        profile = Profile.objects.create(user=user_data, **validated_data)
        profile.user_id = user_data
        return profile


class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)  # use related name

    # profiles = ProfileSerializer()

    class Meta:
        model = User  # 사용할 모델
        fields = ['username', 'password', 'email', 'posts']

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        user = authenticate(username=username, password=password)

        if user is None:
            return {
                'username': 'None'
            }
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given name and password does not exists'
            )
        return {
            'username': user.username,
            'token': jwt_token
        }
