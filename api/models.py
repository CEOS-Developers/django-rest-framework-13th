from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime


class CustomAccountManager(BaseUserManager):
    def create_user(self, username, password):
        user = self.model(username=username, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        print(username)
        return self.get(username)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=32, null=True)
    email = models.EmailField(unique=True, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomAccountManager()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(models.Q(phone__isnull=False) | models.Q(email__isnull=False)),
                name='not_both_null'
            )
        ]

    def natural_key(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    website = models.TextField(max_length=100, blank=True)
    profile_name = models.CharField(max_length=32, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="profileImages", null=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', related_name='posts')
    text = models.TextField(max_length=500, blank=True)
    createdDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', related_name='comments')
    text = models.TextField(max_length=500, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent_id = models.IntegerField()


class Photo(models.Model):
    image = models.ImageField(upload_to='upload_photos/% Y/% m/% d/')  # 어디로 업로드 할지 지정
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='photos')  # 로그인 한 사용자, many to one relation
    pub_date = models.DateTimeField(auto_now_add=True)  # 레코드 생성시 현재 시간으로 자동 생성


class Video(models.Model):
    video = models.ImageField(upload_to='upload_videos/% Y/% m/% d/')  # 어디로 업로드 할지 지정
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='videos')  # 로그인 한 사용자, many to one relation
    pub_date = models.DateTimeField(auto_now_add=True)  # 레코드 생성시 현재 시간으로 자동 생성
