from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import User, Profile, Post


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile  # 사용할 모델
        fields = ['bio', 'user_id']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post  # 사용할 모델
        fields = ['text', 'user', 'createdDate', 'updatedDate']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        post = Post.objects.create(user=user_data, **validated_data)
        post.user_id = user_data
        return post


class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)  # use related name

    class Meta:
        model = User  # 사용할 모델
        fields = ['username', 'password', 'email', 'posts']





