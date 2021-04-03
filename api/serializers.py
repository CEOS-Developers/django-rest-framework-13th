from rest_framework import serializers
from api.models import Profile,Upload

# rest_framework - RESTful한 api를 만들기 위해
# serialize - json형식으로 소통

class UploadSerializer(serializers.ModelSerializer):
    profile_nickname = serializers.SerializerMethodField()  # 함수의 리턴값을 필드로(default=get_~)

    class Meta:
        model = Upload
        fields = '__all__'

    def get_profile_nickname(self, obj):
        return obj.profile.nickname