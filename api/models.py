from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):  # 사용자 모델
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # User 모델에서 OneToOne 확장
    name = models.CharField(max_length=None)  # 사용자의 이름, 중복가능, 글자수 제한 없음
    nickname = models.CharField(max_length=30, blank=False, unique=True)  # 사용자의 닉네임, 글자수 제한 30, 필수입력, 중복 불가능
    intro = models.CharField(max_length=2200)  # 사용자의 자기소개, 글자수 제한 2200
    profile_image = models.ImageField(upload_to='images/', blank=True,
                                      null=True)  # 사용자의 프로필사진, /media/images/에 저장되고 미입력 가능
    website = models.URLField(blank=True)  # 사용자의 웹사이트 url , 중복 가능
    email = models.EmailField(blank=True)  # 사용자의 이메일 주소 , 중복 가능
    phone = models.CharField(blank=False, unique=True)  # 사용자의 전화번호 , 필수입력, 중복 불가능
    birthday = models.DateField(blank=True, null=True)  # 사용자의 생일
