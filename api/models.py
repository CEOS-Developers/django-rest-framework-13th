from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    phone = models.CharField(max_length=32)
    bio = models.TextField(max_length=500, blank=True, NULL=True)
    website = models.TextField(max_length=100, blank=True, NULL=True)
    profile_name = models.TextField(max_length=32, blank=True, NULL=True)
    gender = models.CharField(max_length=10, NULL=True)
    birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to="profileImages")
"""
class follow(models.Model):

class post(models.Model):

class comment(models.Model):

class like(models.Model):

class tag(models.Model):

class location(models.Model):

class photo(models.Model):
    image = models.ImageField(upload_to=user_path)  # 어디로 업로드 할지 지정
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)  # 로그인 한 사용자, many to one relation
    comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)  # 레코드 생성시 현재 시간으로 자동 생성

class video(models.Model):
"""