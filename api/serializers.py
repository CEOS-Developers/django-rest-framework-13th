from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Post, Media, PeopleTag, HashTag


class PeopleTagSerializer(serializers.ModelSerializer):  # PeopleTag model serializer
    class Meta:
        model = PeopleTag
        fields = '__all__'  # all fields in PeopleTag model


class HashTagSerializer(serializers.ModelSerializer):  # HashTag model serializer
    class Meta:
        model = HashTag
        fields = '__all__'  # all fields in HashTag model


class MediaSerializer(serializers.ModelSerializer):  # Media model serializer
    peopletags = PeopleTagSerializer(many=True)  # Media - PeopleTag : ForeignKey

    class Meta:
        model = Media
        fields = ['id', 'upload', 'subs_text', 'peopletags']  # all fields in Media and PeopleTag model


class PostSerializer(serializers.ModelSerializer):  # Post model serializer
    medias = MediaSerializer(many=True)  # Post - Media : ForeignKey
    hashtags = HashTagSerializer(many=True)  # Post - Hashtag : ForeignKey

    class Meta:
        model = Post
        fields = ['id', 'pub_date', 'content', 'location', 'location', 'ratio', 'comment_permission', 'medias', 'hashtags']
        # all fields in Post, Media and Hashtag model


class ProfileSerializer(serializers.ModelSerializer):  # Profile model serializer
    posts = PostSerializer(many=True)  # Profile - Post : ForeignKey

    class Meta:
        model = Profile
        fields = ['id', 'user', 'name', 'nickname', 'intro', 'profile_image', 'website', 'email', 'phone', 'birthday',
                  'gender', 'posts']  # all fields in Profile and Post model


class UserSerializer(serializers.ModelSerializer):  # User model serializer
    profile = ProfileSerializer()  # User - Profile : OneToOneField

    class Meta:
        model = User
        fields = ['username', 'profile']  # username field 만 serialize
