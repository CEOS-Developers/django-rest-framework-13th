from rest_framework import serializers
from .models import *

class HeartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Heart
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    heart_post = HeartSerializer(many=True, read_only=True)
    file_post = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    _following = FollowSerializer(many=True, read_only=True)
    _followed = FollowSerializer(many=True, read_only=True)
    _user = HeartSerializer(many=True, read_only=True)
    _author = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

