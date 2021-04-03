from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import User, Profile, Post


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile  # 사용할 모델
        fields = ['__all__']


class PostSerializer(serializers.ModelSerializer):
    """
    def create(self, validated_data):
        user_data = validated_data.pop('user_id')
        post = Post.objects.create(**validated_data)
        post.user_id.set(user_data)
        return post
    """
    class Meta:
        model = Post  # 사용할 모델
        fields = ['text', 'user_id']


class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)  # use related name

    class Meta:
        model = User  # 사용할 모델
        fields = ['id', 'username', 'posts']





