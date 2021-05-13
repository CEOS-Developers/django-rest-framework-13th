from rest_framework import serializers
from .models import User, Post, Profile


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
    profiles = ProfileSerializer()

    class Meta:
        model = User  # 사용할 모델
        fields = ['username', 'password', 'email', 'posts', 'profiles']








