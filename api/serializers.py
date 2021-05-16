from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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
    def validate(self, data):
        if 'Test' not in data['description']:
            raise ValidationError('Validation Error!')
        return data

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description']

class UploadListSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Upload
        fields = '__all__' # comments 포함해줌

