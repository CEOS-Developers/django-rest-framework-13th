from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, default='')
    phone = models.CharField(max_length=32)
    email = models.EmailField(max_length=254, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    website = models.TextField(max_length=100, blank=True, null=True)
    profile_name = models.CharField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=10, null=True)
    birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="profileImages", null=True)


# related name is used to make two fks from one table
class Follow(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_id')
    following_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following_id')


class Post(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, blank=True, null=True)
    createdDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(blank=True, null=True)


class Comment(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_id = models.IntegerField()


class Like(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)


class Tag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    tagged_id = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Location(models.Model):
    post = models.OneToOneField(
        Post, on_delete=models.CASCADE, primary_key=True,
    )
    place = models.TextField(max_length=100, blank=True)


class Photo(models.Model):
    image = models.ImageField(upload_to='upload_photos/% Y/% m/% d/')  # 어디로 업로드 할지 지정
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 로그인 한 사용자, many to one relation
    pub_date = models.DateTimeField(auto_now_add=True)  # 레코드 생성시 현재 시간으로 자동 생성


class Video(models.Model):
    video = models.ImageField(upload_to='upload_videos/% Y/% m/% d/')  # 어디로 업로드 할지 지정
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 로그인 한 사용자, many to one relation
    pub_date = models.DateTimeField(auto_now_add=True)  # 레코드 생성시 현재 시간으로 자동 생성
