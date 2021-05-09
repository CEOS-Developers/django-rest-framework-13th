from rest_framework import serializers
from api.models import Profile,Upload,Comment

# rest_framework - RESTful한 api를 만들기 위해
# serialize - json형식으로 소통

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'userid', 'userpw', 'nickname', 'user_image']

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description']

class UploadListSerializer(serializers.ModelSerializer): #like, profile fk 추가?
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Upload
        fields = '__all__' # comments 포함해줌

