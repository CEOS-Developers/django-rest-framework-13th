from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Post, Media, PeopleTag, HashTag


class PeopleTagSerializer(serializers.ModelSerializer):  # PeopleTag model serializer
    class Meta:
        model = PeopleTag
        fields = ['media', "name"]


class HashTagSerializer(serializers.ModelSerializer):  # HashTag model serializer
    class Meta:
        model = HashTag
        fields = ['post', "name"]


class MediaSerializer(serializers.ModelSerializer):  # Media model serializer
    peopletags = PeopleTagSerializer(many=True, read_only=True)  # Media - PeopleTag : ForeignKey

    class Meta:
        model = Media
        fields = ['post', 'id', 'upload', 'subs_text', 'peopletags']  # all fields in Media and PeopleTag model


class PostSerializer(serializers.ModelSerializer):  # Post model serializer
    medias = MediaSerializer(many=True, read_only=True)  # Post - Media : ForeignKey
    hashtags = HashTagSerializer(many=True, read_only=True)  # Post - Hashtag : ForeignKey

    class Meta:
        model = Post
        fields = ['profile', 'id', 'pub_date', 'content', 'location', 'ratio', 'comment_permission', 'medias', 'hashtags']
        # all fields in Post, Media and Hashtag model


class ProfileSerializer(serializers.ModelSerializer):  # Profile model serializer
    posts = PostSerializer(many=True, read_only=True)  # Profile - Post : ForeignKey

    class Meta:
        model = Profile
        fields = ['id', 'user', 'name', 'nickname', 'intro', 'profile_image', 'website', 'email', 'phone', 'birthday',
                  'gender', 'posts']  # all fields in Profile and Post model


class UserSerializer(serializers.ModelSerializer):  # User model serializer
    profile = ProfileSerializer(read_only=True)  # User - Profile : OneToOneField

    class Meta:
        model = User
        fields = ['username', 'profile']  # username field 만 serialize
